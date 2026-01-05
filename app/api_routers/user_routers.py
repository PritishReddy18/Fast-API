from sqlalchemy.orm import Session
from app.schemas.validation_schemas.user_schemas import UserCreate
from app.schemas.response_schemas.user_out import UserOut
from app.db.session import get_db
from fastapi import Depends,APIRouter
from app.services.users_services.create_user import create_user
from app.services.users_services.user_login import login_user
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post("/signup",response_model=UserOut)
def sign_up(user: UserCreate , db:Session = Depends(get_db)):
    return create_user(db,user)

@router.post("/login")
def login(user : OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = login_user(user,db)
    return {
        "access_token" : token,
        "token_type" : "bearer"
    }
