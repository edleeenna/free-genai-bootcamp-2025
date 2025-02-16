import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestWordsGroups:
    def test_create_word_group(self, db_session):
        response = client.post("/word_groups/", json={
            "word_id": 2,
            "group_id": 1
        })
        assert response.status_code == 200
        data = response.json()
        assert "word_id" in data
        assert data["group_id"] == 1

    def test_read_word_groups(self, db_session):
        response = client.get("/word_groups/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0
        for item in data:
            assert "word_id" in item
            assert "group_id" in item

    def test_read_word_group(self, db_session):
        response = client.get("/word_groups/1")
        assert response.status_code == 200
        data = response.json()
        assert "word_id" in data
        assert "group_id" in data


    def test_read_word_group_not_found(self, db_session):
        response = client.get("/word_groups/999")
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Word group not found"