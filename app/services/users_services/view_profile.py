from sqlalchemy.orm import Session
from app.orm_models.profile_orm_models import CreateProfile
from fastapi import HTTPException,status

def view_profile_by_id(name : str,db:Session):
    profile = db.query(CreateProfile).filter(CreateProfile.username == name).first()
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user's profile doesn't exist")
    return profile