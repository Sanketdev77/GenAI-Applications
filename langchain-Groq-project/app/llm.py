## this file is responsible for creating LLM object

from langchain_groq import ChatGroq
from app.config import settings

## Create and return langchain LLM
def get_llm():
    return ChatGroq(
        groq_api_key = settings.GROQ_API_KEY,
        model_name = settings.MODEL_NAME,
        temperature= 0.2
    )