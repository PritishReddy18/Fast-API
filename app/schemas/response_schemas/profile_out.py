from pydantic import BaseModel
from datetime import date

class ProfileOut(BaseModel):
    username : str
    date_of_birth : date
    hobby : str
    gender : str
    phone_number : str
    bio : str
    total_posts : int
    total_likes : int

    model_config = {
        "from_attributes" : True
    }