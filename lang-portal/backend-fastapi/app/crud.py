from sqlalchemy.orm import Session
from app import models, schemas

def get_word(db: Session, word_id: int):
    return db.query(models.Word).filter(models.Word.id == word_id).first()

def get_words(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Word).offset(skip).limit(limit).all()

def create_word(db: Session, word: schemas.WordCreate):
    db_word = models.Word(**word.model_dump())
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word

def get_word_review_item(db: Session, item_id: int):
    return db.query(models.WordReviewItem).filter(models.WordReviewItem.id == item_id).first()

def get_word_review_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.WordReviewItem).offset(skip).limit(limit).all()

def create_word_review_item(db: Session, item: schemas.WordReviewItemCreate):
    db_item = models.WordReviewItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Define similar CRUD functions for WordGroup, Group, StudySession, and StudyActivity
def get_word_group(db: Session, word_group_id: int):
    return db.query(models.WordGroup).filter(models.WordGroup.id == word_group_id).first()

def get_word_groups(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.WordGroup).offset(skip).limit(limit).all()

def create_word_group(db: Session, word_group: schemas.WordGroupCreate):
    db_word_group = models.WordGroup(**word_group.model_dump())
    db.add(db_word_group)
    db.commit()
    db.refresh(db_word_group)
    return db_word_group

def get_group(db: Session, group_id: int):
    return db.query(models.Group).filter(models.Group.id == group_id).first()

def get_groups(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Group).offset(skip).limit(limit).all()

def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(**group.model_dump())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def get_study_session(db: Session, study_session_id: int):
    return db.query(models.StudySession).filter(models.StudySession.id == study_session_id).first()

def get_study_sessions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.StudySession).offset(skip).limit(limit).all()

def create_study_session(db: Session, study_session: schemas.StudySessionCreate):
    db_study_session = models.StudySession(**study_session.model_dump())
    db.add(db_study_session)
    db.commit()
    db.refresh(db_study_session)
    return db_study_session

def get_study_activity(db: Session, study_activity_id: int):
    return db.query(models.StudyActivity).filter(models.StudyActivity.id == study_activity_id).first()

def get_study_activities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.StudyActivity).offset(skip).limit(limit).all()

def create_study_activity(db: Session, study_activity: schemas.StudyActivityCreate):
    db_study_activity = models.StudyActivity(**study_activity.model_dump())
    db.add(db_study_activity)
    db.commit()
    db.refresh(db_study_activity)
    return db_study_activity