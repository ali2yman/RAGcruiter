from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    # OPENAI_API_KEY: str

    FILE_ALLOWED_TYPES: List[str]  
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    MONGODB_URL: str
    MONGODB_DATABASE: str

    model_config = SettingsConfigDict(env_file=".env")  #  Pydantic v2 style

def get_settings():
    return Settings()
