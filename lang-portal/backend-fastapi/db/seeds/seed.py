import sys
import os
from sqlalchemy.orm import Session
from app.models import Word, WordGroup, Group, StudySession, StudyActivity, WordReviewItems
from app.database import engine, Base
from datetime import datetime

def seed_data():
    db = Session(bind=engine)

    # Add initial data for words
    words = [
        Word(kanji="例", romaji="rei", english="example", parts="例"),
        Word(kanji="テスト", romaji="tesuto", english="test", parts="テスト"),
    ]
    db.add_all(words)

    # Add initial data for groups
    groups = [
        Group(name="Group 1"),
        Group(name="Group 2"),
    ]
    db.add_all(groups)

    # Add initial data for word groups
    word_groups = [
        WordGroup(word_id=1, group_id=1),
        WordGroup(word_id=2, group_id=2),
    ]
    db.add_all(word_groups)

    # Add initial data for study sessions

    study_sessions = [
        StudySession(group_id=1, session_name="Session 1", created_at=datetime.now(), study_activity_id=1),
        StudySession(group_id=2, session_name="Session 2", created_at=datetime.now(), study_activity_id=3),
    ]
    db.add_all(study_sessions)

    # Add initial data for study activities
    study_activities = [
        StudyActivity(name="Vocabulary Quiz", thumbnail_url="ttps://example.com/vocab-quiz.jpg", description="Practice your vocabulary with flashcards"),
        StudyActivity(name="Writing Practice", thumbnail_url="http://example.com/thumbnail2.png", description="Practice writing Japanese characters"),
    ]
    db.add_all(study_activities)

    # Add initial data for word review items
    word_review_items = [
        WordReviewItems(study_session_id=1, word_id=1, correct=True, created_at=datetime.now()),
        WordReviewItems(study_session_id=2, word_id=2, correct=False, created_at=datetime.now()),
    ]
    db.add_all(word_review_items)

    db.commit()
    db.close()

if __name__ == "__main__":
    seed_data()