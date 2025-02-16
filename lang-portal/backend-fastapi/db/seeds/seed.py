import sys
import os
from sqlalchemy.orm import Session
from app.models import Word, WordGroup, Group, StudySession, StudyActivity, WordReviewItems
from app.database import engine, Base
from datetime import datetime

def seed_data():
    db = Session(bind=engine)

    # Words with more context, focusing on themes like common objects, animals, food, etc.
    words = [
        Word(japanese="例", romaji="rei", english="example", correct_count=10, wrong_count=5),
        Word(japanese="テスト", romaji="tesuto", english="test", correct_count=5, wrong_count=2),
        Word(japanese="学校", romaji="gakkou", english="school", correct_count=8, wrong_count=3),
        Word(japanese="食べ物", romaji="tabemono", english="food", correct_count=12, wrong_count=4),
        Word(japanese="車", romaji="kuruma", english="car", correct_count=6, wrong_count=1),
        Word(japanese="水", romaji="mizu", english="water", correct_count=9, wrong_count=2),
        Word(japanese="家", romaji="ie", english="house", correct_count=7, wrong_count=3),
        Word(japanese="犬", romaji="inu", english="dog", correct_count=14, wrong_count=6),
        Word(japanese="猫", romaji="neko", english="cat", correct_count=11, wrong_count=2),
        Word(japanese="本", romaji="hon", english="book", correct_count=13, wrong_count=5),
        Word(japanese="先生", romaji="sensei", english="teacher", correct_count=15, wrong_count=4),
        Word(japanese="友達", romaji="tomodachi", english="friend", correct_count=10, wrong_count=7),
        Word(japanese="電話", romaji="denwa", english="phone", correct_count=4, wrong_count=1),
        Word(japanese="天気", romaji="tenki", english="weather", correct_count=7, wrong_count=2),
        Word(japanese="料理", romaji="ryouri", english="cooking", correct_count=9, wrong_count=4),
        Word(japanese="旅行", romaji="ryokou", english="travel", correct_count=5, wrong_count=3),
        Word(japanese="音楽", romaji="ongaku", english="music", correct_count=11, wrong_count=6),
        Word(japanese="犬小屋", romaji="inugoya", english="doghouse", correct_count=3, wrong_count=1),
        Word(japanese="ラーメン", romaji="raamen", english="ramen", correct_count=8, wrong_count=2),
        Word(japanese="山", romaji="yama", english="mountain", correct_count=7, wrong_count=4),
        Word(japanese="海", romaji="umi", english="sea", correct_count=10, wrong_count=5),
        Word(japanese="カメラ", romaji="kamera", english="camera", correct_count=12, wrong_count=3),
    ]
    db.add_all(words)

    # Add initial data for groups (grouping by topics like animals, food, weather)
    groups = [
        Group(name="Vocabulary - Everyday Objects"),
        Group(name="Vocabulary - Animals"),
        Group(name="Vocabulary - Weather & Nature"),
        Group(name="Vocabulary - Food & Drink"),
        Group(name="Vocabulary - Technology"),
    ]
    db.add_all(groups)

    # Add initial data for word groups (words associated with specific topics)
    word_groups = [
        WordGroup(word_id=1, group_id=1),  # Example
        WordGroup(word_id=2, group_id=1),
        WordGroup(word_id=3, group_id=1),
        WordGroup(word_id=4, group_id=2),
        WordGroup(word_id=5, group_id=2),
        WordGroup(word_id=6, group_id=3),
        WordGroup(word_id=7, group_id=3),
        WordGroup(word_id=8, group_id=3),
        WordGroup(word_id=9, group_id=4),
        WordGroup(word_id=10, group_id=4),
        WordGroup(word_id=11, group_id=4),
        WordGroup(word_id=12, group_id=4),
        WordGroup(word_id=13, group_id=5),  # Camera in Technology group
        WordGroup(word_id=14, group_id=5),  # Ramen in Food group
        WordGroup(word_id=15, group_id=3),  # Mountain in Nature group
    ]
    db.add_all(word_groups)

    # Add initial data for study sessions
    study_sessions = [
        StudySession(group_id=1, created_at=datetime.now(), study_activity_id=1),
        StudySession(group_id=2, created_at=datetime.now(), study_activity_id=2),
        StudySession(group_id=3,  created_at=datetime.now(), study_activity_id=3),
        StudySession(group_id=4, created_at=datetime.now(), study_activity_id=4),
        StudySession(group_id=5,  created_at=datetime.now(), study_activity_id=5),
    ]
    db.add_all(study_sessions)

    # Add initial data for study activities
    study_activities = [
        StudyActivity(name="Vocabulary Quiz", thumbnail_url="https://example.com/vocab-quiz.jpg", description="Practice your vocabulary with flashcards"),
        StudyActivity(name="Writing Practice", thumbnail_url="http://example.com/thumbnail2.png", description="Practice writing Japanese characters"),
        StudyActivity(name="Kanji Practice", thumbnail_url="https://example.com/kanji-practice.jpg", description="Learn how to write and read Kanji characters"),
        StudyActivity(name="Grammar Quiz", thumbnail_url="https://example.com/grammar-quiz.jpg", description="Test your knowledge of Japanese grammar rules"),
        StudyActivity(name="Technology Quiz", thumbnail_url="https://example.com/tech-quiz.jpg", description="Learn key terms in technology and gadgets"),
    ]
    db.add_all(study_activities)

    # Add initial data for word review items with study sessions
    word_review_items = [
        WordReviewItems(study_session_id=1, word_id=1, correct=True, created_at=datetime.now()),
        WordReviewItems(study_session_id=1, word_id=2, correct=False, created_at=datetime.now()),
        WordReviewItems(study_session_id=2, word_id=4, correct=True, created_at=datetime.now()),
        WordReviewItems(study_session_id=3, word_id=6, correct=True, created_at=datetime.now()),
        WordReviewItems(study_session_id=4, word_id=9, correct=False, created_at=datetime.now()),
        WordReviewItems(study_session_id=5, word_id=13, correct=True, created_at=datetime.now()),
        WordReviewItems(study_session_id=5, word_id=14, correct=False, created_at=datetime.now()),
    ]
    db.add_all(word_review_items)

    db.commit()
    db.close()

if __name__ == "__main__":
    seed_data()
