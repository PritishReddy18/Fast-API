import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

ENV = os.getenv("ENV", "dev")

if ENV == "test":
    DB_URL = "sqlite:///./test.db"
else:
    DB_URL = os.getenv("DATA_BASE")

if not DB_URL:
    raise RuntimeError("DATA_BASE not available")

if DB_URL.startswith("postgresql://"):
    DB_URL = DB_URL.replace("postgresql://", "postgresql+psycopg://", 1)

engine = create_engine(
    DB_URL,
    pool_pre_ping=True,
    connect_args={"check_same_thread": False} if DB_URL.startswith("sqlite") else {}
)

Session = sessionmaker(
    autoflush=False,
    bind=engine
)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()