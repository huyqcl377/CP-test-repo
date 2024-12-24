import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Subject(Base):
    __tablename__ = "subject"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    subject_name = Column(String, index=True)
    credit_num = Column(Integer)
