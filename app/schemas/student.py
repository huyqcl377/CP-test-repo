from pydantic import BaseModel
from datetime import date

class StudentBase(BaseModel):
    full_name: str
    date_of_birth: date
    gender: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True