import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestGroups:
    def test_create_group(self, db_session):
        response = client.post(
            "/groups/",
            json={"name": "Test Group"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Test Group"
        assert "id" in data

    def test_read_groups(self, db_session):
        response = client.get("/groups/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

    def test_read_group(self, db_session):
        # First, create a group to read
        response = client.post(
            "/groups/",
            json={"name": "Test Group"}
        )
        assert response.status_code == 200
        group_id = response.json()["id"]

        # Now, read the group
        response = client.get(f"/groups/{group_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == group_id
        assert data["name"] == "Test Group"

    def test_read_nonexistent_group(self, db_session):
        response = client.get("/groups/9999")
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Group not found"