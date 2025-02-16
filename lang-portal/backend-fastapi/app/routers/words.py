from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/words/", response_model=schemas.Word)
def create_word(word: schemas.WordCreate, db: Session = Depends(get_db)):
    return crud.create_word(db=db, word=word)

@router.get("/words/", response_model=list[schemas.Word])
def read_words(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    words = crud.get_words(db, skip=skip, limit=limit)
    return words

@router.get("/words/{word_id}", response_model=schemas.Word)
def read_word(word_id: int, db: Session = Depends(get_db)):
    db_word = crud.get_word(db, word_id=word_id)
    if db_word is None:
        raise HTTPException(status_code=404, detail="Word not found")
    return db_word
