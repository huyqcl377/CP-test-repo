import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import subjects as models
from schemas import subject as schemas 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@postgres:5432/sample_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/subjects/", response_model=schemas.Subject)
def create_subject(subject: schemas.SubjectCreate, db: Session = Depends(get_db)):
    """
    Create a new subject.
    """
    db_subject = models(**subject.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

@router.get("/subjects/{subject_id}", response_model=schemas.Subject)
def read_subject(subject_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a subject by its UUID.
    """
    try:
        subject_uuid = uuid.UUID(subject_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")
    
    db_subject = db.query(models).filter(models.id == subject_uuid).first()
    if db_subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    return db_subject

@router.put("/subjects/{subject_id}", response_model=schemas.Subject)
def update_subject(subject_id: str, subject_update: schemas.SubjectUpdate, db: Session = Depends(get_db)):
    """
    Update a subject by its UUID.
    """
    try:
        subject_uuid = uuid.UUID(subject_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")
    
    db_subject = db.query(models).filter(models.id == subject_uuid).first()
    if db_subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    
    for key, value in subject_update.dict(exclude_unset=True).items():
        setattr(db_subject, key, value)
    db.commit()
    db.refresh(db_subject)
    return db_subject

@router.delete("/subjects/{subject_id}", response_model=schemas.Subject)
def delete_subject(subject_id: str, db: Session = Depends(get_db)):
    """
    Delete a subject by its UUID.
    """
    try:
        subject_uuid = uuid.UUID(subject_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")
    
    db_subject = db.query(models).filter(models.id == subject_uuid).first()
    if db_subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    
    db.delete(db_subject)
    db.commit()
    return db_subject
