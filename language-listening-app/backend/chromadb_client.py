# chromadb_client.py
import chromadb
from sentence_transformers import SentenceTransformer

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="youtube_transcripts")

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def store_transcript(video_id: str, text: str):
    """Store transcript and embedding in ChromaDB."""
    embedding = embedding_model.encode(text).tolist()
    collection.add(
        ids=[video_id],
        embeddings=[embedding],
        metadatas=[{"video_id": video_id, "text": text}]
    )

def search_transcripts(query: str, n_results=3):
    """Search for relevant transcripts in ChromaDB."""
    results = collection.query(
        query_embeddings=[embedding_model.encode(query).tolist()],
        n_results=n_results
    )
    return results
