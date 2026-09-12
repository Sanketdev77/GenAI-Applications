## this file is responsible for initializing and storing configs

import os
from dotenv import load_dotenv

## 1. load env variable
load_dotenv()

## 2. Read the Groq API key from the env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

## you can add validation

## 3. Model to be used
MODEL = os.getenv("MODEL", "openai/gpt-oss-120b")