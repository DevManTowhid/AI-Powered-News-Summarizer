from fastapi import APIRouter, Body
from app.services.openai_api import summarize_article

router = APIRouter()

@router.post("/")
async def get_summary(content: str = Body(..., embed=True)):
    summary = await summarize_article(content)
    return {"summary": summary}
