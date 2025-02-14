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

@router.post("/word_groups/", response_model=schemas.WordGroup)
def create_word_group(word_group: schemas.WordGroupCreate, db: Session = Depends(get_db)):
    return crud.create_word_group(db=db, word_group=word_group)

@router.get("/word_groups/", response_model=list[schemas.WordGroup])
def read_word_groups(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    word_groups = crud.get_word_groups(db, skip=skip, limit=limit)
    return word_groups

@router.get("/word_groups/{word_group_id}", response_model=schemas.WordGroup)
def read_word_group(word_group_id: int, db: Session = Depends(get_db)):
    db_word_group = crud.get_word_group(db, word_group_id=word_group_id)
    if db_word_group is None:
        raise HTTPException(status_code=404, detail="Word group not found")
    return db_word_group