from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Subject as models
from app.schemas import subjects as schemas
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/subjects/", response_model=schemas.Subject)
def create_subject(subject: schemas.SubjectCreate, db: Session = Depends(get_db)):
    db_subject = models(**subject.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

@router.get("/subjects/{subject_id}", response_model=schemas.Subject)
def read_subject(subject_id: int, db: Session = Depends(get_db)):
    db_subject = db.query(models).filter(models.id == subject_id).first()
    if db_subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    return db_subject
