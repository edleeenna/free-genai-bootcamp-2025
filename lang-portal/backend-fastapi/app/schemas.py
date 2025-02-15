from pydantic import BaseModel
from datetime import datetime

class Config:
    orm_mode = True

# Base schema for Group
class GroupBase(BaseModel):
    name: str

# Schema for creating a new Group
class GroupCreate(GroupBase):
    pass

# Schema for reading a Group, includes id and ORM mode
class Group(GroupBase):
    id: int

    class Config:
        orm_mode = True

# Base schema for StudySession
class StudySessionBase(BaseModel):
    group_id: int
    session_name: str
    created_at: datetime
    study_activity_id: int

# Schema for creating a new StudySession
class StudySessionCreate(StudySessionBase):
    pass

# Schema for reading a StudySession, includes id and ORM mode
class StudySession(StudySessionBase):
    id: int

    class Config:
        orm_mode = True

# Base schema for Word
class WordBase(BaseModel):
    kanji: str
    romaji: str
    english: str
    parts: str = None

# Schema for creating a new Word
class WordCreate(WordBase):
    pass

# Schema for reading a Word, includes id and ORM mode
class Word(WordBase):
    id: int

    class Config:
        orm_mode = True

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

    class Config:
        orm_mode = True

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

    class Config:
        orm_mode = True

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

    class Config:
        orm_mode = True