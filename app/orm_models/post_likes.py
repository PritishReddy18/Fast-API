from app.db.base import Base
from sqlalchemy import Integer,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship

class PostLikes(Base):
    __tablename__ = "likes"
    posts_id : Mapped[int] = mapped_column(Integer,ForeignKey("posts.posts_id", ondelete="CASCADE"),primary_key=True)
    user_id : Mapped[int] = mapped_column(Integer, ForeignKey("users.id",ondelete="CASCADE"), primary_key=True)

    likes = relationship("User",back_populates="users_likes")
    post_id = relationship("CreatePost",back_populates="likes")