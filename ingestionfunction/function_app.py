import azure.functions as func
import logging, requests, os
from concurrent.futures import ThreadPoolExecutor

app = func.FunctionApp()
executor = ThreadPoolExecutor(max_workers=1)

CSV_INGESTION_API_BASE_URL=f"{os.getenv("BACKEND_API_URL")}/ingest_blob_csv"
CONTAINER_NAME=os.getenv("CONTAINER_NAME")
AZURE_APP_SERVICE_URL_FOR_MULTIMODAL_INGESTION=f"{os.getenv("BACKEND_API_URL")}/process_document"

@app.blob_trigger(arg_name="myblob", path="maadendocs/{name}",
                               connection="saknowledgebottest_STORAGE") 
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
        try:
            logging.info(
                f"File {blob_name}. Initiating Request to MultiModal Ingestion"
            )
            executor.submit(send_document_file_async, blob_name, blob_data)
            # mark_blob_as_processed(blob_name)
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send file {blob_name}: {e}")
    else:
        logging.info(
            f"File {blob_name} is a CSV, XLS and XLSX. Initiating request to the CSV, XLS and XLSX Ingestion Pipeline."
        )
        constructed_url = f"{CSV_INGESTION_API_BASE_URL}?container={CONTAINER_NAME}"

        header = {
            "x-api-key": os.getenv("CSV_INGESTION_API_KEY"),
            "accept": "application/json",
        }
        try:
            executor.submit(send_excel_file_async, constructed_url, header)
        except requests.exceptions.RequestException as e:
            logging.error(f"Request to CSV Ingestion Pipeline failed due to: {e}")


def send_document_file_async(blob_name, blob_data):
    try:
        response = requests.post(
            AZURE_APP_SERVICE_URL_FOR_MULTIMODAL_INGESTION,
            files={"file": (blob_name, blob_data)},
        )
        logging.info(
            f"File {blob_name} sent successfully to MultiModal Ingestion Pipeline. Status code: {response.status_code}"
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