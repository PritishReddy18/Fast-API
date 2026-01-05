from app.security.core import pwd_context
from app.core.pepper_config import PEPPER

def password_hasher(password):
    try:
        hashed_password = pwd_context.hash(password + PEPPER)
        return hashed_password
    except Exception:
        raise

def verify_password(current_password,hashed_password):
    try:
        return pwd_context.verify(current_password + PEPPER, hashed_password)
    except Exception:
        return False

def verify_and_upgrade_password(current_password,hashed_password):
    try:
        return pwd_context.verify_and_update(current_password + PEPPER, hashed_password)
    except Exception:
        return False,None