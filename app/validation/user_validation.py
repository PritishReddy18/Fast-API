from sqlalchemy.orm import Session
from app.orm_models.user_orm_models import User
from fastapi import HTTPException,status

def username_validation(db : Session ,username : str):
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='username, already exists')

def email_validation(db:Session,email : str):
    if db.query(User).filter(User.email_id == email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='email, already exists')