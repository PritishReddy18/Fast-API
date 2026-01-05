from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.response_schemas.profile_out import ProfileOut
from app.schemas.validation_schemas.user_schemas import UserProfile
from app.services.users_services.user_profile import create_profile_by_id
from app.orm_models.profile_orm_models import CreateProfile
from app.orm_models.user_orm_models import User
from app.schemas.response_schemas.profle_view import ProfileView
from app.services.users_services.view_profile import view_profile_by_id
from app.security.access_token import get_current_user
from app.orm_models.post_likes import PostLikes
from app.orm_models.posts_orm_model import CreatePost
from sqlalchemy import func

routers = APIRouter(
    prefix="/user/profile",
    tags = ["Users"]
)

@routers.post("/create",response_model=ProfileOut)
def show_profile(profile: UserProfile,user_id: int = Depends(get_current_user),db: Session = Depends(get_db)):
    user_exists = db.query(CreateProfile).filter(CreateProfile.user_id == user_id).first()
    if user_exists is None:
        return create_profile_by_id(profile, user_id, db)
    raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="user already exists")


@routers.get("/view/{name}",response_model=ProfileView)
def view_profile(name,db:Session =Depends(get_db)):
    user = db.query(User).filter(User.username == name).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user doesn't exists")
    profile = view_profile_by_id(name, db)
    return profile

@routers.get("/view",response_model=ProfileOut)
def view_profile_by_token(user_id: int = Depends(get_current_user),db:Session = Depends(get_db)):
    profile = db.query(CreateProfile).filter(CreateProfile.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user's profile doesn't exist!!")
    return profile