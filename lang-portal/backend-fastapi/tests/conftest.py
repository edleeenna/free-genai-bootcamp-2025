import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, get_db, SessionLocal, engine
from db.seeds import seed

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
    seed.seed_data()  # Call the seed function to populate the test database
    try:
        yield db
    finally:
        db.close()