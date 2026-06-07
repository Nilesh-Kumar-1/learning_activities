from fastapi import APIRouter, HTTPException, status, Depends
from functools import lru_cache
from typing import Annotated
from pydantic import BaseModel
from settings import Settings
from services.llm_clients import get_openai_client

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

class ChatMessage(BaseModel):
    message: str

@lru_cache()
def get_settings():
    return Settings() # type: ignore

@router.post("/message", status_code=status.HTTP_200_OK)
async def get_chat_response(message: ChatMessage, settings: Annotated[Settings, Depends(get_settings)]) -> dict:
    """ Python function to call OpenAI models
    
    Keyword arguments:
    message(ChatMessage) -- The chat message to process
    settings(Settings) : Application settings containing OpenAI configuration
    Return:
    dict -- The response from the chat model
    """
    
    # Placeholder for actual chat response logic, e.g., integrating with an AI model
    try:
        if not message.message.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Message cannot be empty"
            )

        gpt_client = get_openai_client(settings)
        response = gpt_client.chat.completions.create(
            model=settings.AZURE_OPENAI_DEPLOYMENT,
            messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.message}
        ],
        temperature=0.7,
        max_tokens=150
        )
    except Exception as e:
        print(f"Error generating response: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate response from LLM"
        )    
    return {"message": response.choices[0].message.content}