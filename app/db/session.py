import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATA_BASE")
if not DB_URL:
    raise RuntimeError('DB_URL not available')
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine,autoflush=False)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()