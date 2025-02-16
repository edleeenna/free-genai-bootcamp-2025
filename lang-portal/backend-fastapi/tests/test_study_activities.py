import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestStudyActivities:
    # Test the /study_activities/ endpoint
    def test_create_study_activity(self, db_session):
        response = client.post("/study_activities/", json={"name": "Activity 1", "thumbnail_url": "http://example.com/thumbnail1.png", "description": "Description 1"})
        assert response.status_code == 200
        assert response.json()["name"] == "Activity 1"
        assert response.json()["thumbnail_url"] == "http://example.com/thumbnail1.png"
        assert response.json()["description"] == "Description 1"

    def test_read_study_activities(self, db_session):
        response = client.get("/study_activities/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_read_study_activity(self, db_session):
        # First, create a study activity
        response = client.post("/study_activities/", json={"name": "Activity 1", "thumbnail_url": "http://example.com/thumbnail1.png", "description": "Description 1"})
        assert response.status_code == 200
        study_activity_id = response.json()["id"]

        # Then, read the created study activity
        response = client.get(f"/study_activities/{study_activity_id}")
        assert response.status_code == 200
        assert response.json()["id"] == study_activity_id

    def test_read_study_sessions(self, db_session):
        # First, create a study activity
        response = client.post("/study_activities/", json={"name": "Activity 1", "thumbnail_url": "http://example.com/thumbnail1.png", "description": "Description 1"})
        assert response.status_code == 200
        study_activity_id = response.json()["id"]

        # Then, read the study sessions for the created study activity
        response = client.get(f"/study_activities/{study_activity_id}/study_sessions")
        assert response.status_code == 200
        assert isinstance(response.json(), list)