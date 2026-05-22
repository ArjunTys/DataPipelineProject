from dotenv import load_dotenv
import os

load_dotenv()
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
if NEWS_API_KEY is None:
    raise ValueError("NEWS_API_KEY not found. Did you create your .env file?")


