from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from app.orm_models.post_likes import PostLikes
from app.orm_models.posts_orm_model import CreatePost
from sqlalchemy.exc import IntegrityError
from app.orm_models.profile_orm_models import CreateProfile


def like_gen(likes):
    if likes.like_post > 1 or likes.like_post < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="only 0 and 1 are allowed, 1 -> like and 0 -> dis like")
    if likes.like_post == 0:
        return False
    return True

def like_system(user_id,likes,db : Session):
    query = db.query(CreatePost).filter(CreatePost.posts_id == likes.post_id).first()
    like_query = db.query(PostLikes).filter(PostLikes.user_id == user_id).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"There are no posts on post_id {likes.post_id}")
    res = like_gen(likes)
    if not res:
        if not like_query:
            raise HTTPException(status_code=status.HTTP_200_OK,detail="You successfully disliked the post")
        db.delete(like_query)

        profile = db.query(CreateProfile).filter(CreateProfile.user_id == user_id).first()
        if not profile:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        profile.total_likes -= 1

        db.commit()

        return {
            "details" : "your like was successfully removed from the post!!"
        }
    new_original_row = PostLikes(
        posts_id=query.posts_id,
        user_id=user_id
    )
    try:
        db.add(new_original_row)

        profile = db.query(CreateProfile).filter(CreateProfile.user_id == user_id).first()
        if not profile:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        profile.total_likes += 1

        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="U have already liked the post!!")
    return {"success": "successfully liked the post"}
