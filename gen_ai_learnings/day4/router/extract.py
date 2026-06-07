from fastapi import APIRouter, HTTPException, status, Depends
from functools import lru_cache
from typing import Annotated, Dict
from pydantic import BaseModel
from settings import Settings
from services.llm_clients import get_document_intelligence_client
from services.document_extraction import extract_text_blob
from services.storage import get_blob_url

router = APIRouter(
    prefix="/extract",
    tags=["extract"]
)

@lru_cache()
def get_settings():
    return Settings() # type: ignore

class ExtractText(BaseModel):
    blob_name: str

@router.post("/text", status_code=status.HTTP_202_ACCEPTED)
async def extract_text(body: ExtractText, settings: Annotated[Settings, Depends(get_settings)]):
    """
    Extract text from pdf
    """
    try:
        print(settings.AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT)
        client = get_document_intelligence_client(settings=settings)
        blob_sas_url = get_blob_url(settings=settings, blob_name=body.blob_name)
        text= extract_text_blob(client=client, blob_sas_url=blob_sas_url)
        return {"message": text}
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"text extraction failed - {e}"
        )