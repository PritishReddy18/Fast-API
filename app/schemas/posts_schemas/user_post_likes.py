from pydantic import BaseModel

class UserPostLikes(BaseModel):
    post_id : int
    like_post : int