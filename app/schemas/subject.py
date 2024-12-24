from pydantic import BaseModel
import uuid

class SubjectBase(BaseModel):
    subject_name: str
    credit_num: int

class SubjectCreate(SubjectBase):
    pass

class SubjectUpdate(SubjectBase):
    name: str | None = None 

class Subject(SubjectBase):
    id: uuid.UUID 

    class Config:
        from_attributes = True
