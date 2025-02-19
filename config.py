import os
from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from .env

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print("GROQ_API_KEY:", GROQ_API_KEY)  # Debug: confirm it prints your key

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in the environment.")