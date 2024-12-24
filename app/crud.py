from sqlalchemy.orm import Session
from app.models import Student, Subject
from app.schemas import student as student_schemas, subject as subject_schemas
import uuid

# CRUD for Students

def get_student(db: Session, student_id: uuid.UUID):
    return db.query(Student).filter(Student.id == student_id).first()

def create_student(db: Session, student_data: student_schemas.StudentCreate):
    db_student = Student(**student_data.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: uuid.UUID, update_data: dict):
    db_student = get_student(db, student_id)
    if db_student:
        for key, value in update_data.items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: uuid.UUID):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student

# CRUD for Subject
def get_subject(db: Session, subject_id: uuid.UUID):
    """
    Retrieve a subject by its UUID.
    """
    return db.query(Subject).filter(Subject.id == subject_id).first()

def create_subject(db: Session, subject_data: subject_schemas.SubjectCreate):
    """
    Create a new subject record.
    """
    db_subject = Subject(**subject_data.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

def update_subject(db: Session, subject_id: uuid.UUID, update_data: dict):
    """
    Update a subject by its UUID.
    """
    db_subject = get_subject(db, subject_id)
    if db_subject:
        for key, value in update_data.items():
            setattr(db_subject, key, value)
        db.commit()
        db.refresh(db_subject)
    return db_subject

def delete_subject(db: Session, subject_id: uuid.UUID):
    """
    Delete a subject by its UUID.
    """
    db_subject = get_subject(db, subject_id)
    if db_subject:
        db.delete(db_subject)
        db.commit()
    return db_subject