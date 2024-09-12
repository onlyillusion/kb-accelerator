# Knowledge Bot HR Accelerator

## Overview

This accelerator enables users to quickly deploy the Azure infrastructure required to run the Knowledge Bot HR application. The chatbot application, which includes both frontend and backend code, is packaged into containers hosted on Azure Container Services. Users can provision the necessary infrastructure with just a few clicks.

### Key Resources Provisioned

The following resources will be deployed automatically as part of this accelerator:

1. **Azure Container Registry (ACR)**: Stores the container images for the chatbot's frontend and backend.
2. **App Service Plan**: A hosting plan for the web applications (frontend and backend) and Function App.
3. **Azure Web Apps**: Two Linux web apps—one for the backend and one for the frontend—both running on containers.
4. **Azure Storage Account**: Stores data, documents, and other files used by the chatbot.
5. **Azure Cognitive Search**: Provides search indexing and query capabilities for uploaded documents.
6. **Azure Redis Cache**: Caching service to optimize application performance.
7. **Azure Key Vault**: Manages secrets and certificates securely, such as API keys and connection strings.
8. **Azure Application Insights**: Provides monitoring and diagnostics for the backend and blob-triggered functions.
9. **Log Analytics Workspace**: Centralized workspace for collecting and analyzing logs.
10. **Azure Function App**: Handles blob storage triggers and other serverless backend operations.
11. **Azure Event Grid**: Manages event routing for storage account events (e.g., blob creation).
12. **Azure OpenAI Service** (Optional): Hosts AI models like GPT-3.5 and GPT-4 for natural language processing in the chatbot.
13. **Azure Document Intelligence**: Enhances the chatbot's ability to understand and extract information from documents.
14. **Azure SQL Database**: Stores relational data for the chatbot's backend.
15. **Managed Identity**: Provides a secure identity for accessing other Azure resources without requiring credentials in code.

Once deployed, the chatbot is ready to be customized with the necessary configurations and integrated with external services like Azure AD for authentication and Azure OpenAI for advanced language capabilities.

---

## Prerequisites

Before deploying the accelerator, ensure you have the following:

1. **GitHub account** (Admin access).
2. **Azure Subscription** with the following:
   - An existing **Azure Resource Group** with **Owner** permissions.
   - **Azure OpenAI** enabled (if using OpenAI models).
   - **Cognitive Services Multi-service account**: Ensure you have accepted the **Responsible AI Terms and Conditions**. [Review terms here](https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account?tabs=multiservice%2Cwindows).
3. **Azure Active Directory (AD)**: Permissions to create an app registration, assign roles, and configure authentication.

---

## Deployment

### Step 1: Deploy Azure Infrastructure

To deploy the necessary Azure infrastructure, click on the appropriate **Deploy to Azure** button below:

- **Without Azure OpenAI**:  
  [![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fasyikinmobiz%2Fkb-accelerator%2Fmain%2Fdeployment%2Foneclick.json)

- **With Azure OpenAI**:  
  [![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2F2Fasyikinmobiz%2Fkb-accelerator%2Fmain%2Fdeployment%2Foneclickaoi.json)

> **Important**: This will provision the infrastructure only. You must complete the following manual steps to finalize the deployment.

---

## Manual Steps After Deployment

### Step 2: Configure Azure AD Authentication

1. Navigate to **Azure Active Directory** in your Azure portal.
2. Select **App Registrations** > **New Registration** to create a new AD app.
3. Under **Redirect URI**, enter the appropriate URL where your frontend is hosted (e.g., the URL of the container in Azure Container Service).
4. Set up the necessary **API permissions**, **roles**, and **groups**:
   - Add any required permissions, such as for Microsoft Graph (e.g., reading user profile data).
   - Configure authentication methods for the app (OAuth2, OpenID Connect, etc.).
5. Save your changes.

### Step 3: Deploy Azure OpenAI Models (If applicable)

If your Knowledge Bot HR integrates with OpenAI models, follow these steps:

1. Navigate to your **Azure OpenAI Resource** in the Azure portal.
2. Go to the **Deployments** tab and create a new deployment for the desired model (e.g., GPT-3.5, GPT-4).
3. Select the **model version**, configure the required parameters, and click **Deploy**.
4. After deployment, note the **endpoint URL** and **API key** as you will need these for configuring the chatbot's backend.

### Step 4: Add Function Code to Azure Function App

1. Go to the **Azure Function App** resource that was provisioned during deployment.
2. In the **Functions** tab, click **Add** to create a new function.
3. Select the appropriate template (Blob Trigger) based on your chatbot logic.
4. Add the **function code** that handles requests to and from the chatbot's backend.
   - use deployment center to deploy code using github connection. Use the ingestionfunction folder for deploying the function code.
5. Save and test the function by uploading a file from the chatbot.

### Step 5: Test Your Deployment

1. Once all steps are complete, navigate to your frontend URL and test the chatbot application.
2. Ensure that the chatbot can authenticate users (via Azure AD), interact with OpenAI models (if applicable), and store results (e.g., in Azure Blob Storage).
3. Monitor logs and errors in Azure Functions and Azure Container Services for debugging.

---

## Additional Resources

- [Azure App Registrations](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Azure OpenAI Documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Azure Functions Documentation](https://docs.microsoft.com/en-us/azure/azure-functions/)

---

## Troubleshooting

- **Authentication issues**: Ensure the redirect URI and permissions are correctly configured in Azure AD.
- **Model deployment issues**: Verify that the correct model is deployed in the Azure OpenAI resource and that the correct API key is used in your application.
- **Azure Function errors**: Check function logs in the Azure portal for detailed error messages.

---

## Contributing

If you have suggestions or find any issues, feel free to open a pull request or raise an issue in the project repository.

## License

This project is licensed under the [MIT License](LICENSE).
