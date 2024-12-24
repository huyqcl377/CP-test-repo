from pydantic_settings  import BaseSettings
import os
import secrets

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings() 
