from app.db.base import Base
from datetime import date
from sqlalchemy import String,Integer,ForeignKey,Date,func
from sqlalchemy.orm import Mapped,mapped_column,relationship

class CreatePost(Base):
    __tablename__ = "posts"
    posts_id : Mapped[int] = mapped_column(Integer,primary_key=True)
    user_id : Mapped[int] = mapped_column(Integer, ForeignKey("users.id",ondelete="CASCADE"), nullable= False,unique=False)
    username : Mapped[str] = mapped_column(String(50),nullable=False)
    title : Mapped[str] = mapped_column(String(100),nullable=False)
    content : Mapped[str] = mapped_column(String(200),nullable=False)
    created_at : Mapped[date] = mapped_column(Date,server_default=func.current_date())

    posts = relationship("User",back_populates="users_posts")
    likes = relationship("PostLikes",back_populates="post_id")