import azure.functions as func
import logging, os
import requests
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
load_dotenv()

app = func.FunctionApp()
executor = ThreadPoolExecutor(max_workers=1)

CONTAINER_NAME=os.getenv("CONTAINER_NAME")
BACKEND_API_URL=os.getenv("BACKEND_API_URL")
BACKEND_API_KEY=os.getenv("BACKEND_API_KEY")

@app.blob_trigger(arg_name="myblob", path=f"{CONTAINER_NAME}/{{name}}",
                               connection="AzureWebJobsStorage") 
def sa_trigger(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
    
    blob_name = myblob.name
    container_name = myblob.uri.split("/")[3]
    full_path = myblob.uri
    
    if not blob_name.endswith((".csv", ".xls", ".xlsx")):
        logging.info(f"File {blob_name} is a PDF.")
        blob_data = myblob.read()
        logging.info(
            f"File {blob_name}. Initiating Request to MultiModal Ingestion"
        )
        constructed_url = f"{BACKEND_API_URL}/process_document"
        logging.info(constructed_url)
        logging.info(f"x-api-key: {BACKEND_API_KEY}")

        header = {
            "x-api-key": BACKEND_API_KEY,
            "accept": "application/json"
        }
        try:
            executor.submit(send_document_file_async, blob_name, blob_data, constructed_url, header)
            # mark_blob_as_processed(blob_name)
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send file {blob_name}: {e}")
    else:
        logging.info(
            f"File {blob_name} is a CSV, XLS and XLSX. Initiating request to the CSV, XLS and XLSX Ingestion Pipeline."
        )
        constructed_url = f"{BACKEND_API_URL}/ingest_blob_csv?container={CONTAINER_NAME}"

        header = {
            "x-api-key": BACKEND_API_KEY,
            "accept": "application/json",
        }
        try:
            executor.submit(send_excel_file_async, constructed_url, header)
        except requests.exceptions.RequestException as e:
            logging.error(f"Request to CSV Ingestion Pipeline failed due to: {e}")


def send_document_file_async(blob_name, blob_data, constructed_url, header):
    try:
        response = requests.post(
            constructed_url,
            files={"file": (blob_name, blob_data)},
            headers=header
        )
        if response.status_code == 200:
            logging.info(
                f"File {blob_name} sent successfully to MultiModal Ingestion Pipeline. Status code: {response.status_code}"
            )
        else:
            logging.error(
                f"Failed to send file {blob_name}. Status code: {response.status_code}. Response: {response.text}"
            )
    except requests.RequestException as exc:
        logging.error(f"An error occurred while sending the file: {exc}")


def send_excel_file_async(constructed_url, header):
    try:
        response = requests.post(constructed_url, headers=header)
        if response.status_code == 200:
            data = response.json()

            logging.info(f"Data Recieved from CSV Ingestion Pipeline: {data}")
    except requests.RequestException as exc:
        logging.error(f"An error occurred while sending the file: {exc}")