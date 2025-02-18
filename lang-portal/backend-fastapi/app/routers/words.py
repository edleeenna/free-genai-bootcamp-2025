from fastapi import APIRouter, Depends, HTTPException, Query
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

@router.get("/words/", response_model=schemas.WordsResponse)
def read_words(
    page: int = Query(1, alias="page"),  # Accept page as a query parameter
    items_per_page: int = Query(10, alias="items_per_page"),  # Accept items_per_page as a query parameter
    db: Session = Depends(get_db)
):
    words = crud.get_words(db, page=page, items_per_page=items_per_page)  # ✅ Pass query params
    return words

@router.get("/words/{word_id}", response_model=schemas.Word)
def read_word(word_id: int, db: Session = Depends(get_db)):
    db_word = crud.get_word(db, word_id=word_id)
    if db_word is None:
        raise HTTPException(status_code=404, detail="Word not found")
    return db_word
