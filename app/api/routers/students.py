from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Student as models
from app.schemas import student as schemas
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(models).filter(models.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student