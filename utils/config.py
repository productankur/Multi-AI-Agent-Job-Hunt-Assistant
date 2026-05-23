import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
USAJOBS_API_KEY = os.getenv("USAJOBS_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
