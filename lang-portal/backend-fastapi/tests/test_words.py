import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestWords:
    def test_create_word(self, db_session):
        response = client.post(
            "/words/",
            json={"japanese": "例", "romaji": "rei", "english": "example", "correct_count": 1, "wrong_count": 1}
        )
        assert response.status_code == 200
        assert response.json()["japanese"] == "例"
        assert response.json()["romaji"] == "rei"

    def test_read_words(self, db_session):
        response = client.get("/words/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_read_word(self, db_session):
        # First, create a word to read
        response = client.post(
            "/words/",
            json={"japanese": "例", "romaji": "rei", "english": "example", "correct_count": 1, "wrong_count": 1}
        )
        word_id = response.json()["id"]

        # Now, read the word
        response = client.get(f"/words/{word_id}")
        assert response.status_code == 200
        assert response.json()["japanese"] == "例"
        assert response.json()["romaji"] == "rei"

    def test_read_nonexistent_word(self, db_session):
        response = client.get("/words/9999")
        assert response.status_code == 404
        assert response.json() == {"detail": "Word not found"}

    def test_update_word(self, db_session):
        # First, create a word to update
        response = client.post(
            "/words/",
            json={"japanese": "例", "romaji": "rei", "english": "example", "correct_count": 1, "wrong_count":2}
        )
        word_id = response.json()["id"]

