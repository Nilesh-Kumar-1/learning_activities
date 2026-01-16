from fastapi import APIRouter, HTTPException, status, Depends, File, UploadFile
from functools import lru_cache
from typing import Annotated
from pydantic import BaseModel
from settings import Settings
from services.azure_clients import get_storage_account_clients
import uuid

router = APIRouter(
    prefix="/storage_account",
    tags=["storage_account"]
)

@lru_cache()
def get_settings() -> Settings:
    return Settings() # type: ignore

@router.post("/upload", status_code=status.HTTP_200_OK)
async def upload_to_storage(settings: Annotated[Settings, Depends(get_settings)], files: list[UploadFile] = File(...)) -> dict:
    """ Python function to demonstrate Azure Storage Account access
    Keyword arguments:
    settings(Settings) : Application settings containing Azure configuration
    Return:
    dict -- Confirmation of storage account access
    """

    try:
        uploaded_files = list()
        storage_client = get_storage_account_clients(setting=settings)
        for file in files:
            extension = file.filename.rsplit(".", 1)[-1].lower() #type: ignore
            if extension not in settings.ALLOWED_FILE_EXTENTION:
                blob_name = f"{uuid.uuid4()}_{file.filename}"

                # Create a blob client using the local file name as the name for the blob
                blob_client = storage_client.get_blob_client(container=settings.AZURE_STORAGE_ACCOUNT_CONTAINER_NAME, blob=blob_name)
                print(f"Uploading to Azure Storage as blob: {file.filename}" )
                # Upload the file
                blob_client.upload_blob(file.file, overwrite=True)
                uploaded_files.append({
                    "original_name": file.filename,
                    "blob_name": blob_name,
                    "container": settings.AZURE_STORAGE_ACCOUNT_CONTAINER_NAME
                })

            else:
                print(f"not a allowed file format: {file.filename}")
                raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"File type not allowed: {file.filename}"
                    )
        return {
            "message": "Files uploaded successfully",
            "file_count": len(files),
            "uploaded_files": uploaded_files
        }

    except Exception as e:
        print(f"Error accessing storage account: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to access Azure Storage Account"
        )