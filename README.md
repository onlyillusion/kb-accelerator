## Overview

This accelerator provides a no code Studio for users to quickly build complex, multi-stage AI pipelines across multiple Azure AI and ML Services.  Users can select, and stack, AI/ML Services from across Azure Cognitive Services (OpenAI, Speech, Language, Form Recognizer, ReadAPI), Azure Machine Learning into a **single**, fully integrated **pipeline**. Integration between services is automated by BPA, and once deployed, a web app is created. This customizable UI&ast; provides and drag-n-drop interface for end users to build multi service pipelines. Finally, the user-created pipeline is triggered as soon as the first input file(s) are uploaded, storing the results in a Azure Blob Storage.

# Deploy to Azure

You can provision Azure resources for the solution accelerator using  the Deploy to Azure button below. You will need to set up an identity provider and specify an admin user

## Deploy to Azure Instructions

### Prerequisities
1. Github account (Admin)
2. Azure Resource Group (Owner)
3. Ensure your subscription has **Microsoft.DocumentDB enabled**  
To confirm/enable:  
      - Navigate to your subscription within portal.azure.com  
      - Select Resource Providers at bottom of left navigation pane  
      - Within the Filter by name menu, search for Microsoft.DocumentDB  
      - Once Microsoft.DocumentDB is found, check if the status is marked as "Registered". If marked as "NotRegistered", Select "Register"  
      **Note**: *This process may take several seconds/minutes, be sure to refresh the entire browser periodically*
4. Ensure that you have **accepted terms and conditions for Responsible AI**:  
You must initiate the creation of a "Cognitive services multi-service account" from the Azure portal to review and acknowledge the terms and conditions. You can do so here: [Quickstart: Create a Cognitive Services resource using the Azure portal](https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account?tabs=multiservice%2Cwindows).  
Once accepted, you can create subsequent resources using any deployment tool (SDK, CLI, or ARM template, etc) under the same Azure subscription.

### Azure Portal Deployment

> [!WARNING]
> This button will only create Azure resources. You will still need to deploy the application by following the deploy to Azure section to build and deploy the application using GitHub actions.

Click on the Deploy to Azure button to deploy the Azure resources for the application.

### Without OpenAI
[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fasyikinmobiz%2Fkb-accelerator%2Fmain%2Fdeployment%2Foneclick.json)

### With OpenAI
[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2F2Fasyikinmobiz%2Fkb-accelerator%2Fmain%2Fdeployment%2Foneclickaoi.json)