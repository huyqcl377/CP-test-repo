
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import FastAPI
# from database import Base, engine
from routers import students, subjects
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@postgres:5432/sample_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


app = FastAPI()

app.include_router(students.router, prefix="/api", tags=["students"])
app.include_router(subjects.router, prefix="/api", tags=["subjects"])