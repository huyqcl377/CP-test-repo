import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from .core.database import Base, settings, get_db_session
from .core.config import settings

# Set up an in-memory SQLite database for testing
DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency for testing
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db_session()] = override_get_db

# Create the test database
Base.metadata.create_all(bind=engine)

# Initialize TestClient
client = TestClient(app)

@pytest.fixture
def db_session():
    """
    Create a new database session for a test.
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# def test_create_subject():
#     """
#     Test creating a new subject.
#     """
#     response = client.post(
#         "/subjects/",
#         json={"name": "Mathematics"}
#     )
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == "Mathematics"
#     assert "id" in data

# def test_read_subject():
#     """
#     Test reading an existing subject by ID.
#     """
#     # Create a subject first
#     create_response = client.post(
#         "/subjects/",
#         json={"name": "Science"}
#     )
#     subject_id = create_response.json()["id"]

#     # Read the subject
#     response = client.get(f"/subjects/{subject_id}")
#     assert response.status_code == 200
#     data = response.json()
#     assert data["id"] == subject_id
#     assert data["name"] == "Science"

# def test_update_subject():
#     """
#     Test updating an existing subject.
#     """
#     # Create a subject first
#     create_response = client.post(
#         "/subjects/",
#         json={"name": "History"}
#     )
#     subject_id = create_response.json()["id"]

#     # Update the subject
#     response = client.put(
#         f"/subjects/{subject_id}",
#         json={"name": "World History"}
#     )
#     assert response.status_code == 200
#     data = response.json()
#     assert data["id"] == subject_id
#     assert data["name"] == "World History"

# def test_delete_subject():
#     """
#     Test deleting an existing subject.
#     """
#     # Create a subject first
#     create_response = client.post(
#         "/subjects/",
#         json={"name": "Geography"}
#     )
#     subject_id = create_response.json()["id"]

#     # Delete the subject
#     response = client.delete(f"/subjects/{subject_id}")
#     assert response.status_code == 200
#     data = response.json()
#     assert data["id"] == subject_id

#     # Verify the subject no longer exists
#     response = client.get(f"/subjects/{subject_id}")
#     assert response.status_code == 404

# def test_invalid_uuid_format():
#     """
#     Test passing an invalid UUID format.
#     """
#     response = client.get("/subjects/invalid-uuid")
#     assert response.status_code == 400
#     assert response.json()["detail"] == "Invalid UUID format"
