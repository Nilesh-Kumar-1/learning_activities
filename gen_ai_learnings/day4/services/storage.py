from settings import Settings
from datetime import datetime, timedelta, timezone
from azure.storage.blob import (
    BlobSasPermissions,
    generate_blob_sas
)

def get_blob_url(settings: Settings, blob_name: str):
    try:
        sas_token = generate_blob_sas(
                account_name=settings.AZURE_STORAGE_ACCOUNT_NAME,
                container_name=settings.AZURE_STORAGE_ACCOUNT_CONTAINER_NAME,
                blob_name=blob_name,
                account_key=settings.AZURE_STORAGE_ACCOUNT_KEY.get_secret_value(),
                permission=BlobSasPermissions(read=True),
                expiry=datetime.now(timezone.utc) + timedelta(hours=1)
            )
        sas_url = (
            f"https://{settings.AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net/"
            f"{settings.AZURE_STORAGE_ACCOUNT_CONTAINER_NAME}/{blob_name}?{sas_token}"
        )
        print("retrieved blob")

    except Exception as e:
        print(f"Error occured while downloading blob - {e}")
        raise

    return sas_url
