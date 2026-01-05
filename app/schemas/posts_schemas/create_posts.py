from pydantic import BaseModel
from datetime import date

class CreatePosts(BaseModel):
    title : str
    content : str

class CreatedPostOut(BaseModel):
    username : str
    title : str
    content : str
    created_at : date

    model_config = {
        "fromm_attributes" : True
    }