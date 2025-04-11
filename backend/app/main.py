from fastapi import FastAPI
from app.api.routes import news, summarize

app = FastAPI(title="AI News Summarizer API")

# Register routes
app.include_router(news.router, prefix="/news", tags=["News"])
app.include_router(summarize.router, prefix="/summarize", tags=["Summarizer"])

