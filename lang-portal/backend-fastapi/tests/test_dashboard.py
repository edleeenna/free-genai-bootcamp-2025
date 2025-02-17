import pytest
from fastapi.testclient import TestClient
from app import models
from app.main import app

client = TestClient(app)

class TestDashboard:
    
    def test_get_last_study_session(self, db_session):
        response = client.get("/dashboard/last-study-session")
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert "group_id" in data
        assert "group_name" in data
        assert "study_activity_id" in data
        assert "start_time" in data
        assert "end_time" in data
        assert "review_items_count" in data

    def test_get_last_study_session_not_found(self, db_session):
        # Empty the database before running this test
        db_session.query(models.StudySession).delete()
        db_session.query(models.Group).delete()
        db_session.query(models.WordReviewItems).delete()
        db_session.commit()
        
        # Assuming the database is empty or the last study session is not found
        response = client.get("/dashboard/last-study-session")
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "No study sessions found"

    def test_get_study_progress(self, db_session):
        response = client.get("/dashboard/study-progress")
        assert response.status_code == 200
        data = response.json()
        assert "total_words_studied" in data
        assert "total_available_words" in data

    def test_get_quick_stats(self, db_session):
        response = client.get("/dashboard/quick-stats")
        assert response.status_code == 200
        data = response.json()
        assert "success_rate" in data
        assert "total_study_sessions" in data
        assert "total_active_groups" in data
        assert "study_streak" in data
        assert "words_learned" in data
        assert "words_in_progress" in data
