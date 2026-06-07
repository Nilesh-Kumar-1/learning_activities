from openai import OpenAI
from settings import Settings
from azure.ai.inference import EmbeddingsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

def get_openai_client(settings: Settings) -> OpenAI:
    """Creates a OpenAI Client
    
    Keyword arguments:
    settings(Settings) : Application settings containing OpenAI configuration
    Return: 
    client(OpenAI) : Configured OpenAI client instance
    """
    
    try:
        client = OpenAI(
                    base_url=settings.AZURE_OPENAI_ENDPOINT,
                    api_key=settings.AZURE_OPENAI_API_KEY.get_secret_value()
                    )
    except Exception as e:
        print("Error creating OpenAI client:", e)
        raise
    return client

def get_openai_embedding_client(settings: Settings) -> EmbeddingsClient:
    """Creates a OpenAI Embedding Client
    
    Keyword arguments:
    settings(Settings) : Application settings containing OpenAI configuration
    Return: 
    client(EmbeddingsClient) : Configured EmbeddingsClient client instance for embeddings
    """
    
    try:
        model = EmbeddingsClient(
            endpoint=settings.AZURE_OPENAI_ENDPOINT,
            credential=AzureKeyCredential(settings.AZURE_OPENAI_EMBEDDING_API_KEY.get_secret_value()),
            model=settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT
        )
    except Exception as e:
        print("Error creating OpenAI embedding client:", e)
        raise
    return model

def get_document_intelligence_client(settings: Settings) -> DocumentIntelligenceClient:
    """Create a Document Intelligence Client

    Keyword arguments:
    settings(Settings) : Application settings containing OpenAI configuration
    Return: 
    client(DocumentIntelligenceClient) : Configured DocumentIntelligenceClient client instance for Document Intelligence
    """
    try:
        document_intelligence_client  = DocumentIntelligenceClient(
            endpoint=settings.AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT,
            credential=AzureKeyCredential(settings.AZURE_DOCUMENT_INTELLIGENCE_KEY.get_secret_value())
            )
        print("created doc int client")
    except Exception as e:
        print(f"Error occured while creating document intelligence client - {e}")
        raise
    return document_intelligence_client