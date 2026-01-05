from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from app.orm_models.posts_orm_model import CreatePost
from app.orm_models.user_orm_models import User
from app.orm_models.profile_orm_models import CreateProfile

def create_user_post(posts,user_id,db : Session):
    fetch_data = db.query(User).filter(User.id == user_id).first()
    if not fetch_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    new_post = CreatePost(
        user_id = fetch_data.id,
        username = fetch_data.username,
        title = posts.title,
        content = posts.content,
    )
    db.add(new_post)
    profile = db.query(CreateProfile).filter(CreateProfile.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    profile.total_posts += 1
    db.commit()
    db.refresh(new_post)
    return new_post