from app.orm_models.user_orm_models import User
from fastapi import HTTPException,status
from app.core.security import verify_password
from app.security.access_token import create_user_token

def login_user(user,db):
    res = db.query(User).filter(User.email_id == user.username).first()
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="there is no user registered with that email id")
    if not verify_password(user.password, res.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="password doesn't match")
    token = create_user_token(res.id)
    return token