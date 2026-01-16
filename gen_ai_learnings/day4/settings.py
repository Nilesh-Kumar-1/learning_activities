from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    """Common Settings
    
    Keyword arguments:
    None
    Return:
    None
    """
    
    AZURE_OPENAI_API_KEY: SecretStr
    AZURE_OPENAI_EMBEDDING_API_KEY: SecretStr
    AZURE_OPENAI_DEPLOYMENT: str
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_API_VERSION: str = "2024-11-20"
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT: str
    AZURE_OPENAI_EMBEDDING_MODEL: str
    AZURE_OPENAI_EMBEDDING_API_VERSION: str = "2024-11-20"
    AZURE_TENANT_ID: str
    AZURE_CLIENT_ID: str
    AZURE_CLIENT_SECRET: SecretStr
    AZURE_STORAGE_ACCOUNT_NAME: str
    AZURE_STORAGE_ACCOUNT_CONTAINER_NAME: str
    ALLOWED_FILE_EXTENTION: list[str]


    model_config = SettingsConfigDict(env_file=".env")