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

@router.post("/word-review-items/", response_model=schemas.WordReviewItems)
def create_word_review_item(item: schemas.WordReviewItemsCreate, db: Session = Depends(get_db)):
    return crud.create_word_review_item(db=db, item=item)

@router.get("/word-review-items/", response_model=list[schemas.WordReviewItems])
def read_word_review_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_word_review_items(db, skip=skip, limit=limit)
    return items

@router.get("/word-review-items/{item_id}", response_model=schemas.WordReviewItems)
def read_word_review_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_word_review_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item