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

@router.post("/groups/", response_model=schemas.Group)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
	return crud.create_group(db=db, group=group)

@router.get("/groups/", response_model=list[schemas.Group])
def read_groups(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
	groups = crud.get_groups(db, skip=skip, limit=limit)
	return groups

@router.get("/groups/{group_id}", response_model=schemas.Group)
def read_group(group_id: int, db: Session = Depends(get_db)):
	db_group = crud.get_group(db, group_id=group_id)
	if db_group is None:
		raise HTTPException(status_code=404, detail="Group not found")
	return db_group
    