from fastapi import APIRouter, HTTPException, status, Depends
from functools import lru_cache
from typing import Annotated, Dict
from pydantic import BaseModel
from settings import Settings
from services.llm_clients import get_openai_embedding_client

router = APIRouter(
    prefix="/similarity",
    tags=["similarity"]
)

@lru_cache
def get_settings() -> Settings:
    return Settings() # type: ignore

class SimilarityRequest(BaseModel):
    texts1: str
    texts2: str

@router.post("/compare", status_code=status.HTTP_200_OK)
async def compare_texts(request: SimilarityRequest, settings: Annotated[Settings, Depends(get_settings)]) -> dict:
    """
    Python function to compare similarity between two texts using OpenAI embeddings
    Keyword arguments:
    request(SimilarityRequest) -- The texts to compare
    settings(Settings) : Application settings containing OpenAI configuration
    Return:
    dict -- The similarity score between the two texts
    """
    try:
        if not request.texts1.strip() or not request.texts2.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Both texts must be non-empty"
            )
        
        embedding_gpt_client = get_openai_embedding_client(settings)
        embedding1 = embedding_gpt_client.embed(
            input=[request.texts1],
        )
        embedding2 = embedding_gpt_client.embed(
            input=[request.texts2]
        )
        print("Embedding 1 Usage:", embedding1.usage)
        print("Embedding 2 Usage:", embedding2.usage)

        # Here you would typically calculate the similarity score between embedding1 and embedding2
        dot_product = sum(float(i) * float(j) for i, j in zip(embedding1.data[0].embedding, embedding2.data[0].embedding))
        print("Dot Product (similarity measure):", dot_product)
        magnitude1 = sum(float(i)**2 for i in embedding1.data[0].embedding) ** 0.5
        magnitude2 = sum(float(i)**2 for i in embedding2.data[0].embedding) ** 0.5
        print("Magnitude 1:", magnitude1)
        print("Magnitude 2:", magnitude2)
        cosine_similarity = dot_product / (magnitude1 * magnitude2)
        print("Cosine Similarity:", cosine_similarity)

    except Exception as e:
        print(f"Error in input validation: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Input validation failed"
        )
    return {"similarity_score": cosine_similarity, "usage" : int(int(embedding1.usage.total_tokens) + int(embedding2.usage.total_tokens))}  # Placeholder for actual similarity score calculation
    

