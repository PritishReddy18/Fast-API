from app.db.base import Base
from sqlalchemy import Integer,String,Date,func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

class User(Base):
    __tablename__ = 'users'
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    username : Mapped[str] = mapped_column(String(18), nullable=False, unique=True)
    email_id : Mapped[str] = mapped_column(String(50),nullable=False,unique=True)
    password_hash : Mapped[str] = mapped_column(String(300),nullable=False)
    created_date : Mapped[date] = mapped_column(Date, server_default=func.current_date(),nullable=False)

    users = relationship(
        "CreateProfile",
        cascade = "all,delete-orphan",
        back_populates="profile"
    )

    users_posts = relationship(
        "CreatePost",
        cascade="all,delete-orphan",
        back_populates="posts"
    )

    users_likes = relationship(
        "PostLikes",
        cascade="all,delete-orphan",
        back_populates="likes"
    )