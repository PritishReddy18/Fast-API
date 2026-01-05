from sqlalchemy.orm import Session
from app.orm_models.posts_orm_model import CreatePost
from fastapi import HTTPException,status

def show_posts(user_id,db: Session):
    posts = db.query(CreatePost).filter(CreatePost.user_id == user_id).all()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="there are no posts of the user!!")
    return posts