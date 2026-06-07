import sys
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from settings import Settings

def get_azure_credential(settings: Settings) -> ClientSecretCredential:
    """Authenticate to Azure using a service principal
    
    Keyword arguments:
    settings(Settings) : Application settings containing Azure configuration
    Return:
    ClientSecretCredential -- The authenticated Azure credential
    """
    try:
        TENANT_ID = settings.AZURE_TENANT_ID
        CLIENT_ID = settings.AZURE_CLIENT_ID
        CLIENT_SECRET = settings.AZURE_CLIENT_SECRET.get_secret_value()
        # Create a credential object
        credential = ClientSecretCredential(
            tenant_id=TENANT_ID,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET
        )

        return credential

    except Exception as e:
        print(f"Authentication failed: {e}", file=sys.stderr)
        raise

def get_storage_account_clients(setting: Settings) -> BlobServiceClient:
    """Create a BlobServiceClient for Azure Storage Account
    
    Keyword arguments:
    settings(Settings) : Application settings containing Azure configuration
    Return:
    BlobServiceClient -- The BlobServiceClient instance
    """

    try:
        credential = get_azure_credential(settings=setting)
        account_url = f"https://{setting.AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net"
        blob_service_client = BlobServiceClient(account_url, credential=credential)
        return blob_service_client

    except Exception as e:
        print(f"Failed to get Azure credential: {e}", file=sys.stderr)
        raise