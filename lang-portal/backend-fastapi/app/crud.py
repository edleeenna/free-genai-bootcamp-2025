from datetime import datetime, timedelta
from sqlalchemy import case, distinct, func, text
from sqlalchemy.orm import Session, aliased
from app import models, schemas

# CRUD function to get a single word by its ID
def get_word(db: Session, word_id: int):
    return db.query(models.Word).filter(models.Word.id == word_id).first()

# CRUD function to get a list of words with pagination
def get_words(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Word).offset(skip).limit(limit).all()

# CRUD function to create a new word in the database
def create_word(db: Session, word: schemas.WordCreate):
    db_word = models.Word(**word.model_dump())  # Map schema to model
    db.add(db_word)
    db.commit()  # Commit the transaction to save the word
    db.refresh(db_word)  # Refresh the instance to get any auto-generated fields (like ID)
    return db_word

# CRUD function to get a single word review item by its ID
def get_word_review_item(db: Session, item_id: int):
    return db.query(models.WordReviewItems).filter(models.WordReviewItems.id == item_id).first()

# CRUD function to get a list of word review items with pagination
def get_word_review_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.WordReviewItems).offset(skip).limit(limit).all()

# CRUD function to create a new word review item
def create_word_review_item(db: Session, item: schemas.WordReviewItemsCreate):
    db_item = models.WordReviewItems(**item.model_dump())  # Map schema to model
    db.add(db_item)
    db.commit()  # Commit the transaction to save the item
    db.refresh(db_item)  # Refresh the instance to get any auto-generated fields
    return db_item

# CRUD function to get a single word group by its ID
def get_word_group(db: Session, word_group_id: int):
    return db.query(models.WordGroup).filter(models.WordGroup.id == word_group_id).first()

# CRUD function to get a list of word groups with pagination
def get_word_groups(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.WordGroup).offset(skip).limit(limit).all()

# CRUD function to create a new word group
def create_word_group(db: Session, word_group: schemas.WordGroupCreate):
    db_word_group = models.WordGroup(**word_group.model_dump())  # Map schema to model
    db.add(db_word_group)
    db.commit()  # Commit the transaction to save the word group
    db.refresh(db_word_group)  # Refresh the instance to get any auto-generated fields
    return db_word_group

# CRUD function to get a single group by its ID
def get_group(db: Session, group_id: int):
    return db.query(models.Group).filter(models.Group.id == group_id).first()

# CRUD function to get a list of groups with pagination
def get_groups(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Group).offset(skip).limit(limit).all()

# CRUD function to create a new group
def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(**group.model_dump())  # Map schema to model
    db.add(db_group)
    db.commit()  # Commit the transaction to save the group
    db.refresh(db_group)  # Refresh the instance to get any auto-generated fields
    return db_group

# CRUD function to get a single study session by its ID
def get_study_session(db: Session, study_session_id: int):
    return db.query(models.StudySession).filter(models.StudySession.id == study_session_id).first()

# CRUD function to get a list of study sessions with paginationfrom sqlalchemy import func
def get_study_sessions(db: Session, skip: int = 0, limit: int = 10):
    results = (
        db.query(
            models.StudySession.id,
            models.StudySession.group_id,
            models.StudySession.created_at,
            models.StudySession.study_activity_id,
            models.Group.name.label("group_name"),
            func.count(models.WordReviewItems.id).label("review_items_count")  # Count the review items
        )
        .join(models.Group)  # Join with Group to get group details
        .outerjoin(models.WordReviewItems, models.WordReviewItems.study_session_id == models.StudySession.id)  # LEFT JOIN with WordReviewItems
        .group_by(models.StudySession.id, models.Group.id)  # Group by study session and group to get counts
        .order_by(models.StudySession.created_at.desc())  # Order by created_at in descending order
        .offset(skip)  # Apply pagination offset
        .limit(limit)  # Apply pagination limit
        .all()  # Fetch the results
    )

    # Ensure each result is correctly mapped to the StudySessionBase schema
    return [
        schemas.StudySessionBase(
            id=session.id,
            group_id=session.group_id,
            group_name=session.group_name,
            activity_id=session.study_activity_id,
            start_time=session.created_at,  # Ensure start_time is set correctly
            end_time=session.created_at,  # Placeholder for end_time
            review_items_count=session.review_items_count,
        )
        for session in results
    ]

# CRUD function to create a new study session
def create_study_session(db: Session, study_session: schemas.StudySessionCreate):
    db_study_session = models.StudySession(**study_session.model_dump())  # Map schema to model
    db.add(db_study_session)
    db.commit()  # Commit the transaction to save the study session
    db.refresh(db_study_session)  # Refresh the instance to get any auto-generated fields
    return db_study_session

# CRUD function to get a single study activity by its ID
def get_study_activity(db: Session, study_activity_id: int):
    return db.query(models.StudyActivity).filter(models.StudyActivity.id == study_activity_id).first()

# CRUD function to get a list of study activities with pagination
def get_study_activities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.StudyActivity).offset(skip).limit(limit).all()

# CRUD function to create a new study activity
def create_study_activity(db: Session, study_activity: schemas.StudyActivityCreate):
    db_study_activity = models.StudyActivity(**study_activity.model_dump())  # Map schema to model
    db.add(db_study_activity)
    db.commit()  # Commit the transaction to save the study activity
    db.refresh(db_study_activity)  # Refresh the instance to get any auto-generated fields
    return db_study_activity

# CRUD function to get study sessions by study activity ID with pagination
def get_study_sessions_by_activity(db: Session, study_activity_id: int, skip: int = 0, limit: int = 10):
      
    results = (
        db.query(
            models.StudySession.id,
            models.StudySession.group_id,
            models.Group.name.label("group_name"),
            models.StudySession.study_activity_id.label("activity_id"),
            models.StudySession.created_at.label("start_time"),
            func.count(models.WordReviewItems.id).label("review_items_count")
        )
        .join(models.Group, models.Group.id == models.StudySession.group_id)
        .outerjoin(models.WordReviewItems, models.WordReviewItems.study_session_id == models.StudySession.id)
        .filter(models.StudySession.study_activity_id == study_activity_id)  # activity_id comes from the URL path
        .group_by(
            models.StudySession.id,
            models.StudySession.group_id,
            models.Group.name,
            models.StudySession.study_activity_id,
            models.StudySession.created_at,
        )
        .all()
    )
    
        # Ensure each result is correctly mapped to the StudySessionBase schema
    return [
        schemas.StudySessionBase(
            id=session.id,
            group_id=session.group_id,
            group_name=session.group_name,
            activity_id=study_activity_id,
            start_time=session.start_time,  # Ensure start_time is set correctly
            end_time=session.start_time,  # Placeholder for end_time
            review_items_count=session.review_items_count,
        )
        for session in results
    ]
# Function to get the last study session (for dashboard)
def get_last_study_session(db: Session):
    result = db.query(models.StudySession.id,
                       models.StudySession.group_id,
                       models.StudySession.created_at,
                       models.StudySession.study_activity_id,
                       models.Group.name).join(models.Group).order_by(models.StudySession.created_at.desc()).first()
    if result:
    # Convert the result tuple to a dictionary
        return {
            "id": result.id,
            "group_id": result.group_id,
            "created_at": result.created_at,
            "study_activity_id": result.study_activity_id,
            "group_name": result.name
        }
    return None

# Function to calculate study progress for the dashboard
def get_study_progress(db: Session):
    total_words_studied = db.query(func.count(func.distinct(models.WordReviewItems.word_id))).scalar()  # Count distinct studied words
    total_available_words = db.query(func.count(models.Word.id)).scalar()  # Assuming 'id' is the primary key of the Word model
  # Count total available words
    return schemas.StudyProgress(
        total_words_studied=total_words_studied,
        total_available_words=total_available_words,  
    )

# Function to calculate quick stats for the dashboard
def get_quick_stats(db: Session):
    total_study_sessions = db.query(models.StudySession).count()  # Count total study sessions
    total_active_groups_count = total_active_groups(db)  # Call another function to calculate active groups
    success_rate_value = success_rate(db)  # Call function to calculate success rate
    study_streak_value = study_streak(db)  # Call function to calculate study streak
    words_learned = db.query(func.count(func.distinct(models.WordReviewItems.word_id))
                         .filter(models.WordReviewItems.correct == True)).scalar()
    words_in_progress = db.query(func.count(func.distinct(models.WordReviewItems.word_id))
                             .filter(models.WordReviewItems.correct == False)).scalar()

    return schemas.QuickStats(
        success_rate=success_rate_value,
        total_study_sessions=total_study_sessions,
        total_active_groups=total_active_groups_count,
        study_streak=study_streak_value,
        words_learned=words_learned,
        words_in_progress=words_in_progress,
    )

# Function to calculate the success rate of word review items
def success_rate(db: Session):
    success_rate_query = db.query(
        (func.coalesce(func.sum(
            case(
                (models.WordReviewItems.correct == True, 1),  # Pass condition as positional arguments
                else_=0
            )
        ) * 1.0 /
         func.nullif(func.count(models.WordReviewItems.id), 0) * 100, 0.0)).label('success_rate'),
        
        func.coalesce(func.count(
            query = db.query(models.WordReviewItems.word_id).filter(models.WordReviewItems.correct == True).distinct()

        ), 0).label('correct_words'),
        
        func.coalesce(func.count(
            query = db.query(models.WordReviewItems.word_id).filter(models.WordReviewItems.correct == False).distinct()
        ), 0).label('incorrect_words')
    ).one()

    return success_rate_query.success_rate  # Return the success rate

def study_streak(db: Session):
    yesterday = datetime.now() - timedelta(days=1)  # Get yesterday's date

    # Create an alias for the study sessions table for recursive query emulation
    study_sessions = aliased(models.StudySession)

    # Subquery to get distinct study dates
    dates_subquery = db.query(func.date(models.StudySession.created_at).label('study_date')) \
        .group_by(func.date(models.StudySession.created_at)) \
        .order_by(func.date(models.StudySession.created_at).desc()) \
        .subquery()

    # Create the streak subquery as a select statement
    streak_subquery = db.query(
        dates_subquery.c.study_date,
        func.row_number().over(order_by=dates_subquery.c.study_date.desc()).label('streak')
    ).filter(
        dates_subquery.c.study_date >= yesterday.strftime('%Y-%m-%d')
    ).subquery()  # Ensure it's treated as a subquery

    # Get the maximum streak from the subquery
    max_streak = db.query(func.coalesce(func.max(streak_subquery.c.streak), 0)).scalar()

    return max_streak  # Return the maximum streak


# Function to calculate the total number of active groups in the last 30 days
def total_active_groups(db: Session):
    thirty_days_ago = datetime.now() - timedelta(days=30)  # Get the date 30 days ago
    
    # Query to count distinct group IDs where created_at is within the last 30 days
    active_groups_count = db.query(func.count(func.distinct(models.StudySession.group_id))) \
                            .filter(models.StudySession.created_at >= thirty_days_ago) \
                            .scalar()
    
    return active_groups_count if active_groups_count else 0  # Return the count of active groups
