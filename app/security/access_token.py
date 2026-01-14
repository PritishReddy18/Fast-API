from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import ExpiredSignatureError,JWTError
from fastapi import HTTPException,status,Depends
from app.core.environmental_variables import TOKEN_EXPIRE_IN_MINUTES, PRIVATE_KEY, ALGORITHM, PUBLIC_KEY
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

def create_user_token(user_id):
    payload = {"sub" : str(user_id), "exp" : datetime.utcnow() + timedelta(minutes=int(TOKEN_EXPIRE_IN_MINUTES))}
    token = jwt.encode(payload,PRIVATE_KEY,algorithm=ALGORITHM)
    return token

def get_current_user(token : str = Depends(oauth2_scheme)):
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Not authenticated buffalo")

    try:
        payload = jwt.decode(
            token,
            PUBLIC_KEY,
            algorithms=[ALGORITHM]
        )
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Token Expired")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Token")
    current_user = (payload.get("sub"))
    if current_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid token")
    try:
        current_user_id = int(current_user)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="user id not found")
    return current_user_id