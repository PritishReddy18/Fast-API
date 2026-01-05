from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from app.core.security import verify_password
from app.orm_models.user_orm_models import User
from app.orm_models.profile_orm_models import CreateProfile

def create_profile_by_id(profile,user_id : int,db:Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    if not verify_password(profile.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="password doesn't match")

    new_user = CreateProfile(
        user_id = user.id,
        username = user.username,
        date_of_birth = profile.date_of_birth,
        hobby = profile.hobby,
        gender = profile.gender,
        phone_number = profile.phone_number,
        bio = profile.bio,
        total_posts = 0,
        total_likes = 0,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

