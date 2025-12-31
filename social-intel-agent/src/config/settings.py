from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    redis_url: str = "redis://localhost:6379"
    mongo_url: str = "mongodb+srv://atharvgangwar8_db_user:GsVUGRlzjBgC9RBW@smarttaskmanager.u4hiott.mongodb.net/studyplanner?retryWrites=true&w=majority"
    log_level: str = "INFO"
    api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    huggingface_token: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings()