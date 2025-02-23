# models.py
from pydantic import BaseModel

class TranscriptRequest(BaseModel):
    video_id: str

class SearchRequest(BaseModel):
    query: str
