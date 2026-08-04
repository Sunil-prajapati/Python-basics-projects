import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Settings:
    origins = os.getenv("ORIGINS")

settings = Settings()