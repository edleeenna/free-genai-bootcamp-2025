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

@router.post("/study_sessions/", response_model=schemas.StudySession)
def create_study_session(study_session: schemas.StudySessionCreate, db: Session = Depends(get_db)):
    return crud.create_study_session(db=db, study_session=study_session)

@router.get("/study_sessions/", response_model=list[schemas.StudySession])
def read_study_sessions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    study_sessions = crud.get_study_sessions(db, skip=skip, limit=limit)
    return study_sessions

@router.get("/study_sessions/{study_session_id}", response_model=schemas.StudySession)
def read_study_session(study_session_id: int, db: Session = Depends(get_db)):
    db_study_session = crud.get_study_session(db, study_session_id=study_session_id)
    if db_study_session is None:
        raise HTTPException(status_code=404, detail="Study session not found")
    return db_study_session

@router.post("/study_activities/", response_model=schemas.StudyActivity)
def create_study_activity(study_activity: schemas.StudyActivityCreate, db: Session = Depends(get_db)):
    return crud.create_study_activity(db=db, study_activity=study_activity)

@router.get("/study_activities/", response_model=list[schemas.StudyActivity])
def read_study_activities(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    study_activities = crud.get_study_activities(db, skip=skip, limit=limit)
    return study_activities

@router.get("/study_activities/{study_activity_id}", response_model=schemas.StudyActivity)
def read_study_activity(study_activity_id: int, db: Session = Depends(get_db)):
    db_study_activity = crud.get_study_activity(db, study_activity_id=study_activity_id)
    if db_study_activity is None:
        raise HTTPException(status_code=404, detail="Study activity not found")
    return db_study_activity