from fastapi import APIRouter,HTTPException,status,Depends
from app.services.posts_services.create_post_service import create_user_post
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.schemas.posts_schemas.create_posts import CreatePosts,CreatedPostOut
from app.security.access_token import get_current_user
from app.services.posts_services.show_posts import show_posts
from app.schemas.posts_schemas.user_post_likes import UserPostLikes
from app.services.posts_services.post_user_like import like_system

router = APIRouter(
    prefix="/user",
    tags=["Posts"]
)

@router.post("/create/post",response_model=CreatedPostOut)
def create_post(posts:CreatePosts,user_id : int = Depends(get_current_user),db:Session = Depends(get_db)):
    return create_user_post(posts,user_id,db)


@router.get("/posts")
def show_user_post(user_id : int = Depends(get_current_user), db : Session = Depends(get_db)):
    return show_posts(user_id,db)

@router.post("/post/like")
def like_post(likes : UserPostLikes, user_id : int = Depends(get_current_user), db:Session = Depends(get_db)):
    return like_system(user_id,likes,db)