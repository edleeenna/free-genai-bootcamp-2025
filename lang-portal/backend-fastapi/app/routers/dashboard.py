from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/dashboard/last-study-session", response_model=schemas.LastStudySession)
def get_last_study_session(db: Session = Depends(get_db)):
    last_session = crud.get_last_study_session(db)
    if last_session is None:
        raise HTTPException(status_code=404, detail="No study sessions found")
    print(last_session) 
    return last_session

@router.get("/dashboard/study-progress", response_model=schemas.StudyProgress)
def get_study_progress(db: Session = Depends(get_db)):
    return crud.get_study_progress(db)

@router.get("/dashboard/quick-stats", response_model=schemas.QuickStats)
def get_quick_stats(db: Session = Depends(get_db)):
    return crud.get_quick_stats(db)