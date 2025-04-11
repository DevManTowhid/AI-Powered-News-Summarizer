import httpx
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

async def fetch_top_headlines():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "apiKey": NEWS_API_KEY,
        "pageSize": 5,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.json()
