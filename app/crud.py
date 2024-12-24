from sqlalchemy.orm import Session
from app.models import Subject, Score
from app.schemas import student as student_schemas, subjects as subject_schemas, scores as score_schemas
from app.models import students

# CRUD for Students

def get_student(db: Session, student_id: int):
    return db.query(students.Student).filter(students.Student.id == student_id).first()

def create_student(db: Session, student_data: student_schemas.StudentCreate):
    db_student = students.Student(**student_data.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, update_data: dict):
    db_student = get_student(db, student_id)
    if db_student:
        for key, value in update_data.items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student
