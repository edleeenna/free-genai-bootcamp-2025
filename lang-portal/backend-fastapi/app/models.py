from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    kanji = Column(String, index=True, nullable=False)
    romaji = Column(String, index=True, nullable=False)
    english = Column(String, index=True, nullable=False)
    parts = Column(String)

class WordGroup(Base):
    __tablename__ = 'words_groups'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    word_id = Column(Integer, ForeignKey('words.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)

class StudySession(Base):
    __tablename__ = 'study_sessions'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey('groups.id'))
    session_name = Column(String, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    study_activity_id = Column(Integer, ForeignKey('study_activities.id'), nullable=False)

class StudyActivity(Base):
    __tablename__ = 'study_activities'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    thumbnail_url = Column(String, index=True)
    description = Column(String, index=True)

class WordReviewItems(Base):
    __tablename__ = 'word_review_items'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    study_session_id = Column(Integer, ForeignKey('study_sessions.id'))
    word_id = Column(Integer, ForeignKey('words.id'), nullable=False)
    correct = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
