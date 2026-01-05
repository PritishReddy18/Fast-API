from app.orm_models.user_orm_models import User
from sqlalchemy.orm import Session
from app.core.security import password_hasher
from app.validation.user_validation import username_validation,email_validation

def create_user(db : Session,user):
    username_validation(db,user.username)
    email_validation(db,user.email_id)
    new_user = User(
        username = user.username,
        email_id = user.email_id,
        password_hash = password_hasher(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user