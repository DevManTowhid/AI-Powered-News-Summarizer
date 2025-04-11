# AI-Powered News Summarizer – Backend

FastAPI backend for fetching top news articles and generating summaries using OpenAI's GPT.

## Endpoints

- `GET /news` — Fetches top news articles
- `POST /summarize` — Returns summary of a given article content

## Running Locally

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
