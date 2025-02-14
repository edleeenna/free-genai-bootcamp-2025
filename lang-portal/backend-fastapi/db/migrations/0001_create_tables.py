from sqlalchemy import create_engine, MetaData
from app.models import Base

DATABASE_URL = "sqlite:///./words.db"

def run_migrations():
    engine = create_engine(DATABASE_URL)
    metadata = MetaData()

     # Drop all tables
    Base.metadata.drop_all(engine)

    # Create all tables
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    run_migrations()