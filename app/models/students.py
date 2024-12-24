import uuid
from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    full_name = Column(String, index=True)
    date_of_birth = Column(Date)
    gender = Column(String)
