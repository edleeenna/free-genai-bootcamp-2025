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
        # Everyday Objects
        Word(japanese="時計", romaji="tokei", english="clock", correct_count=3, wrong_count=1),
        Word(japanese="椅子", romaji="isu", english="chair", correct_count=6, wrong_count=2),
        Word(japanese="机", romaji="tsukue", english="desk", correct_count=4, wrong_count=1),
        Word(japanese="窓", romaji="mado", english="window", correct_count=5, wrong_count=2),
        Word(japanese="扉", romaji="tobira", english="door", correct_count=7, wrong_count=3),
        # Animals
        Word(japanese="鳥", romaji="tori", english="bird", correct_count=8, wrong_count=3),
        Word(japanese="魚", romaji="sakana", english="fish", correct_count=5, wrong_count=1),
        Word(japanese="馬", romaji="uma", english="horse", correct_count=3, wrong_count=2),
        Word(japanese="象", romaji="zou", english="elephant", correct_count=6, wrong_count=4),
        Word(japanese="猿", romaji="saru", english="monkey", correct_count=2, wrong_count=1),
        # Food & Drink
        Word(japanese="りんご", romaji="ringo", english="apple", correct_count=4, wrong_count=2),
        Word(japanese="お茶", romaji="ocha", english="tea", correct_count=7, wrong_count=1),
        Word(japanese="ビール", romaji="biiru", english="beer", correct_count=6, wrong_count=3),
        Word(japanese="ピザ", romaji="piza", english="pizza", correct_count=8, wrong_count=2),
        Word(japanese="寿司", romaji="sushi", english="sushi", correct_count=5, wrong_count=4),
        Word(japanese="牛肉", romaji="gyuuniku", english="beef", correct_count=10, wrong_count=3),
        Word(japanese="野菜", romaji="yasai", english="vegetables", correct_count=3, wrong_count=1),
        Word(japanese="水", romaji="mizu", english="water", correct_count=9, wrong_count=2),
        # Weather & Nature
        Word(japanese="晴れ", romaji="hare", english="sunny", correct_count=8, wrong_count=3),
        Word(japanese="雨", romaji="ame", english="rain", correct_count=5, wrong_count=2),
        Word(japanese="風", romaji="kaze", english="wind", correct_count=6, wrong_count=3),
        Word(japanese="雪", romaji="yuki", english="snow", correct_count=7, wrong_count=1),
        Word(japanese="虹", romaji="niji", english="rainbow", correct_count=4, wrong_count=1),
        Word(japanese="森林", romaji="shinrin", english="forest", correct_count=9, wrong_count=5),
        Word(japanese="海", romaji="umi", english="sea", correct_count=10, wrong_count=3),
        Word(japanese="山", romaji="yama", english="mountain", correct_count=6, wrong_count=2),
        # Transportation
        Word(japanese="車", romaji="kuruma", english="car", correct_count=8, wrong_count=3),
        Word(japanese="自転車", romaji="jitensha", english="bicycle", correct_count=5, wrong_count=1),
        Word(japanese="飛行機", romaji="hikouki", english="airplane", correct_count=9, wrong_count=4),
        Word(japanese="電車", romaji="densha", english="train", correct_count=6, wrong_count=2),
        Word(japanese="船", romaji="fune", english="ship", correct_count=7, wrong_count=3),
        # Technology & Gadgets
        Word(japanese="パソコン", romaji="pasokon", english="personal computer", correct_count=4, wrong_count=1),
        Word(japanese="スマートフォン", romaji="sumaatofon", english="smartphone", correct_count=8, wrong_count=5),
        Word(japanese="テレビ", romaji="terebi", english="television", correct_count=7, wrong_count=2),
        Word(japanese="カメラ", romaji="kamera", english="camera", correct_count=9, wrong_count=3),
        Word(japanese="冷蔵庫", romaji="reizouko", english="refrigerator", correct_count=10, wrong_count=4),
        Word(japanese="ゲーム", romaji="geemu", english="game", correct_count=3, wrong_count=2),
        # Emotions & Feelings
        Word(japanese="幸せ", romaji="shiawase", english="happiness", correct_count=7, wrong_count=2),
        Word(japanese="悲しい", romaji="kanashii", english="sad", correct_count=6, wrong_count=1),
        Word(japanese="怒る", romaji="okoru", english="angry", correct_count=5, wrong_count=3),
        Word(japanese="楽しい", romaji="tanoshii", english="fun", correct_count=9, wrong_count=4),
        Word(japanese="怖い", romaji="kowai", english="scary", correct_count=4, wrong_count=2),
        Word(japanese="驚く", romaji="odoroku", english="surprised", correct_count=6, wrong_count=3),
        # Education
        Word(japanese="先生", romaji="sensei", english="teacher", correct_count=10, wrong_count=5),
        Word(japanese="学生", romaji="gakusei", english="student", correct_count=7, wrong_count=2),
        Word(japanese="教室", romaji="kyoushitsu", english="classroom", correct_count=5, wrong_count=1),
        Word(japanese="本", romaji="hon", english="book", correct_count=8, wrong_count=4),
        Word(japanese="大学", romaji="daigaku", english="university", correct_count=6, wrong_count=3),
        Word(japanese="勉強", romaji="benkyou", english="study", correct_count=3, wrong_count=2),
    ]
    db.add_all(words)

    # Add initial data for groups (grouping by topics like animals, food, weather)
    groups = [
        Group(name="Vocabulary - Everyday Objects", word_count=5),
        Group(name="Vocabulary - Animals", word_count=5),
        Group(name="Vocabulary - Food & Drink", word_count=8),
        Group(name="Vocabulary - Weather & Nature", word_count=8),
        Group(name="Vocabulary - Transportation", word_count=5),
        Group(name="Vocabulary - Technology", word_count=6),
        Group(name="Vocabulary - Emotions & Feelings", word_count=6),
        Group(name="Vocabulary - Education", word_count=6),
    ]
    db.add_all(groups)

# Add initial data for word groups (words associated with specific topics)
    word_groups = [
        WordGroup(word_id=1, group_id=1),
        WordGroup(word_id=2, group_id=1),
        WordGroup(word_id=3, group_id=1),
        WordGroup(word_id=4, group_id=1),
        WordGroup(word_id=5, group_id=1),
        WordGroup(word_id=6, group_id=2),
        WordGroup(word_id=7, group_id=2),
        WordGroup(word_id=8, group_id=2),
        WordGroup(word_id=9, group_id=2),
        WordGroup(word_id=10, group_id=2),
        WordGroup(word_id=11, group_id=3),
        WordGroup(word_id=12, group_id=3),
        WordGroup(word_id=13, group_id=3),
        WordGroup(word_id=14, group_id=3),
        WordGroup(word_id=15, group_id=3),
        WordGroup(word_id=16, group_id=4),
        WordGroup(word_id=17, group_id=4),
        WordGroup(word_id=18, group_id=4),
        WordGroup(word_id=19, group_id=4),
        WordGroup(word_id=20, group_id=4),
        WordGroup(word_id=21, group_id=5),
        WordGroup(word_id=22, group_id=5),
        WordGroup(word_id=23, group_id=5),
        WordGroup(word_id=24, group_id=5),
        WordGroup(word_id=25, group_id=5),
        WordGroup(word_id=26, group_id=6),
        WordGroup(word_id=27, group_id=6),
        WordGroup(word_id=28, group_id=6),
        WordGroup(word_id=29, group_id=6),
        WordGroup(word_id=30, group_id=6),
        WordGroup(word_id=31, group_id=7),
        WordGroup(word_id=32, group_id=7),
        WordGroup(word_id=33, group_id=7),
        WordGroup(word_id=34, group_id=7),
        WordGroup(word_id=35, group_id=7),
        WordGroup(word_id=36, group_id=8),
        WordGroup(word_id=37, group_id=8),
        WordGroup(word_id=38, group_id=8),
        WordGroup(word_id=39, group_id=8),
        WordGroup(word_id=40, group_id=8),
    ]
    db.add_all(word_groups)

    # Add initial data for study activities
    study_activities = [
        StudyActivity(name="Vocabulary Quiz", thumbnail_url="https://example.com/vocab-quiz.jpg", description="Practice your vocabulary with flashcards"),
        StudyActivity(name="Writing Practice", thumbnail_url="http://example.com/thumbnail2.png", description="Practice writing Japanese characters"),
        StudyActivity(name="Kanji Practice", thumbnail_url="https://example.com/kanji-practice.jpg", description="Learn how to write and read Kanji characters"),
        StudyActivity(name="Grammar Quiz", thumbnail_url="https://example.com/grammar-quiz.jpg", description="Test your knowledge of Japanese grammar rules"),
        StudyActivity(name="Technology Quiz", thumbnail_url="https://example.com/tech-quiz.jpg", description="Learn key terms in technology and gadgets"),
    ]
    db.add_all(study_activities)

    # Add initial data for study sessions (without start_time and end_time to avoid the error)
    study_sessions = [
        StudySession(group_id=1, study_activity_id=1),
        StudySession(group_id=2, study_activity_id=2),
        StudySession(group_id=3, study_activity_id=3),
        StudySession(group_id=4, study_activity_id=4),
        StudySession(group_id=5, study_activity_id=5),
    ]
    db.add_all(study_sessions)

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
