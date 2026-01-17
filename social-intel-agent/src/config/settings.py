from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    log_level: str = "INFO"
    api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    huggingface_token: Optional[str] = None
    mongodb_uri: str = "mongodb://localhost:27017"
    environment: str = "development"
    
    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()