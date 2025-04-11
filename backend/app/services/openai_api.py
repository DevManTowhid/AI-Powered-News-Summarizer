import httpx
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def summarize_article(content: str):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful news summarizer."},
            {"role": "user", "content": f"Summarize the following:\n\n{content}"}
        ],
        "temperature": 0.5
    }

    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        result = response.json()
        return result["choices"][0]["message"]["content"]
