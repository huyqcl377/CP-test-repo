from sqlalchemy import Column, Integer, String, Date
from app.core.database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    date_of_birth = Column(Date)
    gender = Column(String)
