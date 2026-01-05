from pydantic import BaseModel

class UserOut(BaseModel):
    id : int
    username : str
    email_id : str

    model_config = {
        "from_attributes" : True
    }