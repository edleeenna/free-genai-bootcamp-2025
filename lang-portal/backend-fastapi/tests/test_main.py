import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, get_db, SessionLocal, engine

# Set TESTING flag to use the test database
os.environ["TESTING"] = "1"

# Create a TestClient instance
client = TestClient(app)

# Create test database tables
Base.metadata.create_all(bind=engine)

# Dependency override to use test database
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Test the /words/ endpoint
def test_create_word(db_session):
    response = client.post("/words/", json={"japanese": "例", "romaji": "rei", "english": "example", "correct_count": "1", "wrong_count": "1"})
    assert response.status_code == 200
    assert response.json()["japanese"] == "例"

def test_read_words(db_session):
    response = client.get("/words/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_word(db_session):
    response = client.get("/words/1")
    assert response.status_code == 200
    assert response.json()["japanese"] == "例"

# Test the /groups/ endpoint
def test_create_group(db_session):
    response = client.post("/groups/", json={"name": "Group 1"})
    assert response.status_code == 200
    assert response.json()["name"] == "Group 1"

def test_read_groups(db_session):
    response = client.get("/groups/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_group(db_session):
    response = client.get("/groups/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Group 1"

# Test the /study_sessions/ endpoint
def test_create_study_session(db_session):
    response = client.post("/study_sessions/", json={"group_id": 1, "session_name": "Session 1", "created_at": "2023-01-01T00:00:00", "study_activity_id": 2})
    assert response.status_code == 200
    assert response.json()["session_name"] == "Session 1"

def test_read_study_sessions(db_session):
    response = client.get("/study_sessions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_study_session(db_session):
    response = client.get("/study_sessions/1")
    assert response.status_code == 200
    assert response.json()["session_name"] == "Session 1"

# Test the /study_activities/ endpoint
def test_create_study_activity(db_session):
    response = client.post("/study_activities/", json={"name": "Activity 1", "thumbnail_url": "http://example.com/thumbnail1.png", "description": "Description 1"})
    assert response.status_code == 200
    assert response.json()["name"] == "Activity 1"

def test_read_study_activities(db_session):
    response = client.get("/study_activities/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_study_activity(db_session):
    response = client.get("/study_activities/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Activity 1"

# Test the /word_review_items/ endpoint
def test_create_word_review_item(db_session):
    response = client.post("/word_review_items/", json={"study_session_id": 1, "word_id": 1, "correct": True, "created_at": "2023-01-01T00:00:00"})
    assert response.status_code == 200
    assert response.json()["correct"] == True

def test_read_word_review_items(db_session):
    response = client.get("/word_review_items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_word_review_item(db_session):
    response = client.get("/word_review_items/1")
    assert response.status_code == 200
    assert response.json()["correct"] == True