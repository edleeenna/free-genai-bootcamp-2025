from typing import List
from pydantic import BaseModel
from datetime import datetime

class ConfigDict:
    from_attributes = True

# Pagination schema
class Pagination(BaseModel):
    current_page: int
    total_pages: int
    items_per_page: int

# Base schema for Group
class GroupBase(BaseModel):
    name: str

# Schema for creating a new Group
class GroupCreate(GroupBase):
    pass

# Schema for reading a Group, includes id and ORM mode
class Group(GroupBase):
    id: int

    class ConfigDict:
        from_attributes = True

# Base schema for StudySession
class StudySessionBase(BaseModel):
    id: int
    group_id: int
    group_name: str
    study_activity_id: int
    start_time: datetime
    end_time: datetime
    review_items_count: int
    
# Schema for creating a new StudySession
class StudySessionCreate(BaseModel):
    group_id: int
    created_at: datetime  # Required only for creation, not for the response
    study_activity_id: int

# Schema for reading a StudySession, includes id and ORM mode
class StudySession(StudySessionBase):
    id: int

    class ConfigDict:
        from_attributes = True

# Base schema for Word
class WordBase(BaseModel):
    japanese: str
    romaji: str
    english: str
    correct_count: int
    wrong_count: int

    class ConfigDict:
        from_attributes = True


# Schema for creating a new Word
class WordCreate(WordBase):
    pass

# Schema for reading a Word, includes id and ORM mode
class Word(WordBase):
    id: int

    class ConfigDict:
        from_attributes = True

# Base schema for WordGroup
class WordGroupBase(BaseModel):
    word_id: int
    group_id: int

# Schema for creating a new WordGroup
class WordGroupCreate(WordGroupBase):
    pass

# Schema for reading a WordGroup, includes id and ORM mode
class WordGroup(WordGroupBase):
    id: int

    class ConfigDict:
        from_attributes = True

class WordsResponse(BaseModel):
    items: List[Word]
    pagination: Pagination

# Base schema for StudyActivity
class StudyActivityBase(BaseModel):
    name: str
    thumbnail_url: str = None
    description: str = None

# Schema for creating a new StudyActivity
class StudyActivityCreate(StudyActivityBase):
    pass

# Schema for reading a StudyActivity, includes id and ORM mode
class StudyActivity(StudyActivityBase):
    id: int

    class ConfigDict:
        from_attributes = True

# Base schema for WordReviewItem
class WordReviewItemsBase(BaseModel):
    study_session_id: int
    word_id: int
    correct: bool
    created_at: datetime

# Schema for creating a new WordReviewItems
class WordReviewItemsCreate(WordReviewItemsBase):
    pass

# Schema for reading a WordReviewItems, includes id and ORM mode
class WordReviewItems(WordReviewItemsBase):
    id: int

    class ConfigDict:
        from_attributes = True

        # dashboard/last_study_session
class LastStudySession(BaseModel):
    id: int
    group_id: int
    group_name: str
    study_activity_id: int
    start_time: datetime
    end_time: datetime
    review_items_count: int

    class ConfigDict:
        from_attributes = True

# dashboard/study_progress
class StudyProgress(BaseModel):
    total_words_studied: int
    total_available_words: int

# dashboard/quick_stats
class QuickStats(BaseModel):
    success_rate: float
    total_study_sessions: int
    total_active_groups: int
    study_streak: int
    words_learned: int
    words_in_progress: int