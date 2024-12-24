from pydantic import BaseModel
from datetime import date
import uuid

class StudentBase(BaseModel):
    full_name: str
    date_of_birth: date
    gender: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: uuid.UUID 

    class Config:
        from_attributes = True