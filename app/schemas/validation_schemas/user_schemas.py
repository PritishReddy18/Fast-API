from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import date


class UserCreate(BaseModel):
    username : str
    email_id : EmailStr
    password : str

class UserProfile(BaseModel):
    password : str
    date_of_birth : date = Field(
        examples=["2001-08-15"],
        description="Date of birth in YYYY-MM-DD format"
    )
    hobby : str
    gender : str
    phone_number : str
    bio : Optional[str]

    @field_validator("date_of_birth")
    @classmethod
    def dob_validator(cls,dob : date):
        if dob > date.today():
            raise ValueError("Date of birth cannot be in future!! u dumb ass alien")
        return dob