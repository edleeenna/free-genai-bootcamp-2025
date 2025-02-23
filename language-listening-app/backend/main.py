# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import chromadb_client
import youtube_transcript
import question_generator
from models import TranscriptRequest, SearchRequest

# Initialize FastAPI
app = FastAPI()

# Store Transcript Endpoint
@app.post("/store_transcript")
def store_transcript(request: TranscriptRequest):
    """Fetches, processes, and stores a YouTube transcript in ChromaDB."""
    text = youtube_transcript.get_youtube_transcript(request.video_id)
    if not text:
        raise HTTPException(status_code=404, detail="Transcript not found.")
    
    chromadb_client.store_transcript(request.video_id, text)
    return {"message": f"Stored transcript for video: {request.video_id}"}

# Search Transcripts Endpoint
@app.post("/search")
def search_transcripts(request: SearchRequest):
    """Search for relevant transcripts in ChromaDB."""
    results = chromadb_client.search_transcripts(request.query)
    if not results["metadatas"]:
        raise HTTPException(status_code=404, detail="No matching transcripts found.")
    
    response = [
        {"video_id": metadata.get("video_id", "Unknown"), "excerpt": metadata.get("text", "")[:300]}
        for metadata in results["metadatas"][0]
    ]
    return response

# Generate Questions Endpoint
@app.post("/generate_questions")
def generate_questions(request: TranscriptRequest):
    """Generate multiple-choice questions based on a YouTube transcript."""
    results = chromadb_client.collection.get(ids=[request.video_id])
    if not results["metadatas"]:
        raise HTTPException(status_code=404, detail="Transcript not found.")
    
    transcript_text = results["metadatas"][0]["text"]
    questions = question_generator.generate_questions(request.video_id, transcript_text)
    
    if not questions:
        raise HTTPException(status_code=500, detail="Error generating questions.")
    
    return questions
