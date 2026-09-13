import os

from dotenv import load_dotenv

## 1. load env variables from .env file
load_dotenv()

## Storage of application configs in one place
class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    MODEL_NAME = os.getenv("MODEL_NAME")


## Create one settings object that can be imported throughout the application
settings = Settings()