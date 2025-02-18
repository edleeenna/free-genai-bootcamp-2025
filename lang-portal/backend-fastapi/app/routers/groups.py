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

@router.post("/groups/", response_model=schemas.Group)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
	return crud.create_group(db=db, group=group)

@router.get("/groups/", response_model=schemas.GroupsResponse)
def read_groups(
    page: int = Query(1, alias="page"),  # Accept page as a query parameter
    items_per_page: int = Query(10, alias="items_per_page"),  # Accept items_per_page as a query parameter
    db: Session = Depends(get_db)
):
    groups = crud.get_groups(db, page=page, items_per_page=items_per_page)  # Pass query params
    return groups

@router.get("/groups/{group_id}", response_model=schemas.Group)
def read_group(group_id: int, db: Session = Depends(get_db)):
	db_group = crud.get_group(db, group_id=group_id)
	if db_group is None:
		raise HTTPException(status_code=404, detail="Group not found")
	return db_group
    
@router.get("/groups/{group_id}/words", response_model=schemas.WordsResponse)
def read_group_words( 
	group_id: int,
	page: int = Query(1, alias="page"),  # Accept page as a query parameter
    items_per_page: int = Query(10, alias="items_per_page"),  # Accept items_per_page as a query parameter
    db: Session = Depends(get_db)
	):
    db_words = crud.get_group_words(db, group_id=group_id)
    if db_words is None:
        raise HTTPException(status_code=404, detail="Words not found for the group")
    return db_words
    
from fastapi import Query

@router.get("/groups/{group_id}/study-sessions", response_model=schemas.StudySessionResponse)
def read_study_sessions_by_group(
    group_id: int,
    page: int = Query(1, alias="page", ge=1),  # Page number must be at least 1
    items_per_page: int = Query(10, alias="items_per_page", le=100),  # Max 100 per page
    db: Session = Depends(get_db)
):
  
    skip = (page - 1) * items_per_page
    result = crud.get_study_sessions_by_group(db, group_id=group_id, skip=skip, limit=items_per_page)

    if not result["items"]:
        raise HTTPException(status_code=404, detail="No study sessions found for this group")

    return result
