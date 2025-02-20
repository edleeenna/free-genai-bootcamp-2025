from datetime import datetime, timedelta
from fastapi import HTTPException
from sqlalchemy import case, distinct, func, text
from sqlalchemy.orm import Session, aliased
from app import models, schemas

# CRUD function to get a single word by its ID
def get_word(db: Session, word_id: int):
    return db.query(models.Word).filter(models.Word.id == word_id).first()

def get_words(db: Session, page: int = 1, items_per_page: int = 10):
    # Calculate skip (number of records to skip)
    skip = (page - 1) * items_per_page

    words = db.query(models.Word).offset(skip).limit(items_per_page).all()
    total_count = db.query(models.Word).count()  # Get total word count

    # Convert ORM objects to Pydantic models
    word_items = [schemas.Word.model_validate(word, from_attributes=True) for word in words]

    # Calculate total pages
    total_pages = (total_count // items_per_page) + (1 if total_count % items_per_page > 0 else 0)

    # Debugging logs
    print(f"Fetching words for page={page}, items_per_page={items_per_page}, skip={skip}")
    print(f"Total words in DB: {total_count}, Total pages: {total_pages}")

    return schemas.WordsResponse(
        items=word_items,
        pagination=schemas.Pagination(
            current_page=page,  # ✅ Fix: Return the actual page number
            total_pages=total_pages,
            items_per_page=items_per_page
        )
    )


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

def get_groups(db: Session, page: int = 1, items_per_page: int = 10):
    # Calculate skip (number of records to skip)
    skip = (page - 1) * items_per_page

    groups = db.query(models.Group).offset(skip).limit(items_per_page).all()  # Query paginated groups
    total_count = db.query(models.Group).count()  # Get total number of groups

    # Convert ORM objects to Pydantic models
    group_items = [schemas.Group.model_validate(group, from_attributes=True) for group in groups]

    # Calculate total pages
    total_pages = (total_count // items_per_page) + (1 if total_count % items_per_page > 0 else 0)

    # Debugging logs (can be removed later)
    print(f"Fetching groups for page={page}, items_per_page={items_per_page}, skip={skip}")
    print(f"Total groups in DB: {total_count}, Total pages: {total_pages}")

    return schemas.GroupsResponse(
        items=group_items,
        pagination=schemas.Pagination(
            current_page=page,  # Return the actual page number
            total_pages=total_pages,
            items_per_page=items_per_page,
        )
    )

# CRUD function to create a new group
def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(**group.model_dump())  # Map schema to model
    db.add(db_group)
    db.commit()  # Commit the transaction to save the group
    db.refresh(db_group)  # Refresh the instance to get any auto-generated fields
    return db_group

def get_group_words(db: Session, group_id: int, page: int = 1, items_per_page: int = 10):
    # Calculate skip (number of records to skip)
    skip = (page - 1) * items_per_page

    words = db.query(models.Word).join(models.WordGroup, models.Word.id == models.WordGroup.word_id).filter(models.WordGroup.group_id == group_id).offset(skip).limit(items_per_page).all()
    
    total_count = db.query(models.Word).join(models.WordGroup, models.Word.id == models.WordGroup.word_id).filter(models.WordGroup.group_id == group_id).count()

    # Calculate total pages
    total_pages = (total_count // items_per_page) + (1 if total_count % items_per_page > 0 else 0)

    return {
        "items": words,
        "pagination": {
            "current_page": page,
            "total_pages": total_pages,
            "items_per_page": items_per_page
        }
    }


def get_study_session(db: Session, study_session_id: int):
    result = (
        db.query(
            models.StudySession.id,
            models.StudySession.group_id,
            models.StudySession.created_at.label("start_time"),
            models.StudySession.study_activity_id.label("study_activity_id"),
            models.StudyActivity.name.label("study_activity_name"),
            # Assuming end_time is the same as created_at for this example
            models.StudySession.created_at.label("end_time"),
            models.Group.name.label("group_name"),
            func.count(models.WordReviewItems.id).label("review_items_count")
        )
        .join(models.Group, models.Group.id == models.StudySession.group_id)
        .join(models.StudyActivity, models.StudyActivity.id == models.StudySession.study_activity_id)
        .outerjoin(models.WordReviewItems, models.WordReviewItems.study_session_id == models.StudySession.id)
        .filter(models.StudySession.id == study_session_id)
        .group_by(models.StudySession.id, models.Group.id)
        .first()
    )
    
    if result:
        # Map the tuple result to a dictionary that matches your schema
        return {
            "id": result.id,
            "group_id": result.group_id,
            "group_name": result.group_name,
            "study_activity_id": result.study_activity_id,
            "study_activity_name": result.study_activity_name,
            "start_time": result.start_time,
            "end_time": result.end_time,
            "review_items_count": result.review_items_count
        }
    return None

# CRUD function to get a list of study sessions with pagination
def get_study_sessions(db: Session, skip: int = 0, limit: int = 10):
    # Get total count of study sessions
    total_count = db.query(func.count(models.StudySession.id)).scalar()

    # Fetch paginated study sessions
    results = (
        db.query(
            models.StudySession.id,
            models.StudySession.group_id,
            models.StudySession.created_at,
            models.StudySession.study_activity_id,
            models.Group.name.label("group_name"),
            models.StudyActivity.name.label("study_activity_name"),
            func.count(models.WordReviewItems.id).label("review_items_count")  # Count review items
        )
        .join(models.Group, models.Group.id == models.StudySession.group_id)  # Join with Group
        .join(models.StudyActivity, models.StudyActivity.id == models.StudySession.study_activity_id)  # Join with StudyActivity
        .outerjoin(models.WordReviewItems, models.WordReviewItems.study_session_id == models.StudySession.id)  # LEFT JOIN with WordReviewItems
        .group_by(models.StudySession.id, models.Group.id, models.StudyActivity.id)  # Group by required fields
        .order_by(models.StudySession.created_at.desc())  # Order by most recent session
        .offset(skip)  # Apply pagination offset
        .limit(limit)  # Apply pagination limit
        .all()  # Fetch results
    )

    return {
        "items": [
            schemas.StudySessionBase(
                id=session.id,
                group_id=session.group_id,
                group_name=session.group_name,
                study_activity_id=session.study_activity_id,
                study_activity_name=session.study_activity_name,
                start_time=session.created_at,  # Start time from created_at
                end_time=session.created_at,  # Placeholder for end_time
                review_items_count=session.review_items_count,
            )
            for session in results
        ],
        "pagination": {
            "current_page": (skip // limit) + 1,
            "total_pages": (total_count + limit - 1) // limit,  # Calculate total pages
            "items_per_page": limit,
        },
    }

# CRUD function to get a single study session by its ID
# CRUD function to get study sessions by group
def get_study_sessions_by_group(
    db: Session, group_id: int, skip: int = 0, limit: int = 10
):
    total_count = db.query(func.count(models.StudySession.id)).filter(models.StudySession.group_id == group_id).scalar()

    results = (
        db.query(
            models.StudySession.id,
            models.StudySession.group_id,
            models.StudySession.created_at,
            models.StudySession.study_activity_id,
            models.Group.name.label("group_name"),
            models.StudyActivity.name.label("study_activity_name"),  # Get study activity name
            func.count(models.WordReviewItems.id).label("review_items_count")  # Count review items
        )
        .join(models.Group, models.Group.id == models.StudySession.group_id)  # Join with Group to get group details
        .join(models.StudyActivity, models.StudyActivity.id == models.StudySession.study_activity_id)  # Join with StudyActivity
        .outerjoin(models.WordReviewItems, models.WordReviewItems.study_session_id == models.StudySession.id)  # LEFT JOIN with WordReviewItems
        .filter(models.StudySession.group_id == group_id)  # Filter by group_id
        .group_by(models.StudySession.id, models.Group.id, models.StudyActivity.id)  # Group by session, group, and study activity
        .order_by(models.StudySession.created_at.desc())  # Order by most recent session
        .offset(skip)  # Pagination offset
        .limit(limit)  # Pagination limit
        .all()
    )

    return {
        "items": [
            schemas.StudySessionBase(
                id=session.id,
                group_id=session.group_id,
                group_name=session.group_name,
                study_activity_id=session.study_activity_id,
                study_activity_name=session.study_activity_name,  # Include study activity name
                start_time=session.created_at,  # Start time from created_at
                end_time=session.created_at,  # Placeholder for end_time
                review_items_count=session.review_items_count,
            )
            for session in results
        ],
        "pagination": {
            "current_page": (skip // limit) + 1,
            "total_pages": (total_count + limit - 1) // limit,
            "items_per_page": limit,
        },
    }



def create_study_session(db: Session, study_session: schemas.StudySessionCreate):
    # Create a StudySession model object from the input data
    db_study_session = models.StudySession(
        group_id=study_session.group_id,
        created_at=study_session.created_at,
        study_activity_id=study_session.study_activity_id,
        # You can add any other required fields here, or set defaults as needed
    )
    
    # Assuming you have a method to get the group name, you can populate it here
    group = db.query(models.Group).filter(models.Group.id == study_session.group_id).first()
    if group:
        db_study_session.group_name = group.name  # Assign group name to the session

    # Set default values for start_time, end_time, or calculate them
    db_study_session.start_time = study_session.created_at  # You can adjust this as needed
    db_study_session.end_time = study_session.created_at  # Adjust this based on your logic

    # You can also calculate the review_items_count if it's based on some logic
    db_study_session.review_items_count = 0  # Default, or calculate based on study activity

    # Add the study session to the session and commit
    db.add(db_study_session)
    db.commit()
    db.refresh(db_study_session)  # Refresh to get any auto-generated fields like ID

    # Return the created study session
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
    result = ( db.query(
            models.StudySession.id,
            models.StudySession.group_id,
            models.StudySession.created_at,
            models.StudySession.study_activity_id,
            models.Group.name.label("group_name"),
            func.count(models.WordReviewItems.id).label("review_items_count")
        )
        .join(models.Group)  # Join with Group to get group details
        .outerjoin(models.WordReviewItems, models.WordReviewItems.study_session_id == models.StudySession.id)  # LEFT JOIN with WordReviewItems
        .group_by(models.StudySession.id, models.Group.id)  # Group by study session and group to get counts
        .order_by(models.StudySession.created_at.desc())
        .first()
    )
    if result:
    # Convert the result tuple to a dictionary
        return {
            "id": result.id,
            "group_id": result.group_id,
            "group_name": result.group_name,
            "study_activity_id": result.study_activity_id,
            "start_time": result.created_at,
            "end_time": result.created_at,
            "review_items_count": result.review_items_count,
        }
    return None
def get_words_for_study_session(db: Session, study_session_id: int, page: int = 1, items_per_page: int = 20):
    # Calculate offset for pagination
    offset = (page - 1) * items_per_page
    
    # Fetch words for the study session with basic join and filter to debug
    words = (
        db.query(
            models.Word.id,
            models.Word.japanese,
            models.Word.romaji,
            models.Word.english,
            models.Word.correct_count,
            models.Word.wrong_count,
            models.Group.name.label("group_name"),
        )
        .join(models.WordReviewItems, models.WordReviewItems.word_id == models.Word.id)
        .join(models.StudySession, models.StudySession.id == models.WordReviewItems.study_session_id)
        .join(models.Group, models.Group.id == models.StudySession.group_id)  # Join with Group via StudySession
        .filter(models.StudySession.id == study_session_id)  # Only filter by study_session_id first
        .offset(offset)
        .limit(items_per_page)
        .all()
    )
    
    # Add a debug statement to print out the words for this query
    print(f"Found {len(words)} words for study session ID: {study_session_id}")
    
    return words



      # Return a list of WordBase schemas, but use tuple indexing to access columns
    return [
        schemas.WordBase(
            japanese=word[1],  # word[1] corresponds to models.Word.japanese
            romaji=word[2],    # word[2] corresponds to models.Word.romaji
            english=word[3],   # word[3] corresponds to models.Word.english
            correct_count=word[4],  # word[4] corresponds to models.Word.correct_count
            wrong_count=word[5]     # word[5] corresponds to models.Word.wrong_count
        )
        for word in words
    ]
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
