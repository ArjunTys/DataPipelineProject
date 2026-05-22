import requests
from utils.config import NEWS_API_KEY

def fetch_news(q, language = 'en', pageSize = 100):
    headers = {
        "X-Api-Key":NEWS_API_KEY

    }

    params = {
        "q": q,
        "language": language,
        "pageSize": pageSize

    }

    url = "https://newsapi.org/v2/everything"

    response = requests.get(url, headers=headers, params=params, timeout=30)

    response.raise_for_status()

    return response.json()
