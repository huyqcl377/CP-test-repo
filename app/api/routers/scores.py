from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import scores as models
from app.schemas import scores as schemas
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/scores/", response_model=schemas.Score)
def create_score(score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    db_score = models.Score(**score.dict())
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

@router.get("/scores/{score_id}", response_model=schemas.Score)
def read_score(score_id: int, db: Session = Depends(get_db)):
    db_score = db.query(models.Score).filter(models.Score.id == score_id).first()
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score
