from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey,Date
from typing import Optional
from datetime import date

class CreateProfile(Base):
    __tablename__ = "profile"
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    user_id : Mapped[Optional[int]] = mapped_column(ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    username : Mapped[Optional[str]] = mapped_column(String(100),nullable=True)
    date_of_birth : Mapped[date] = mapped_column(Date,nullable=False)
    hobby : Mapped[str] = mapped_column(String(50),nullable=False)
    gender : Mapped[str] = mapped_column(String(7),nullable=False)
    phone_number : Mapped[int] = mapped_column(String(11),nullable=False)
    bio : Mapped[Optional[str]] = mapped_column(String,nullable=True)
    total_posts : Mapped[int] = mapped_column(Integer,nullable=True)
    total_likes : Mapped[int] = mapped_column(Integer,nullable=True)
    profile = relationship("User",back_populates="users")