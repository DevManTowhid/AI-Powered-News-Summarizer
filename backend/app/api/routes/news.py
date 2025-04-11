from fastapi import APIRouter
from app.services.news_api import fetch_top_headlines

router = APIRouter()

@router.get("/")
async def get_top_news():
    return await fetch_top_headlines()

