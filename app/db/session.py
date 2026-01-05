import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

if DB_URL.startswith("postgresql://"):
    DB_URL = DB_URL.replace("postgresql://", "postgresql+psycopg://", 1)

if not DB_URL:
    raise RuntimeError('DB_URL not available')

engine = create_engine(
    DB_URL,
    pool_pre_ping=True
)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()