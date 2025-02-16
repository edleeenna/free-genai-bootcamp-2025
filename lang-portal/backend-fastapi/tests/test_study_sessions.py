import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestStudySessions:
    def test_read_study_sessions(self, db_session):
        response = client.get("/study-sessions/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0
        for item in data:
            assert "id" in item
            assert "group_id" in item
            assert "group_name" in item
            assert "study_activity_id" in item
            assert "start_time" in item
            assert "end_time" in item
            assert "review_items_count" in item

    def test_read_study_session(self, db_session):
        response = client.get("/study-sessions/1")
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert "group_id" in data
        assert "group_name" in data
        assert "study_activity_id" in data
        assert "start_time" in data
        assert "end_time" in data
        assert "review_items_count" in data

    def test_read_study_session_not_found(self, db_session):
        response = client.get("/study-sessions/999")
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Study session not found"

    def test_get_words_for_study_session(self, db_session):
        response = client.get("/study-sessions/1/words")
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0
        for item in data:
            assert "japanese" in item
            assert "romaji" in item

    def test_get_words_for_study_session_not_found(self, db_session):
        response = client.get("/study-sessions/999/words")
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Words not found"