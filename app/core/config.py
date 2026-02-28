import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "FastAPI Car Price Project"
    API_KEY: str = os.getenv("API_KEY","demo-key")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = "HS256"
    REDIS_URL: str = os.getenv("REDIS_URL")
    MODEL_PATH: str = "app/models/model.pkl"

settings = Settings()