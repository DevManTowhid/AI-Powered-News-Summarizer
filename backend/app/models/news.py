from pydantic import BaseModel

class NewsArticle(BaseModel):
    title: str
    description: str | None
    url: str
    source: dict
