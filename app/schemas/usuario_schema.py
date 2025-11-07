from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    display_name: str
    avatar_url: Optional[HttpUrl] = None
    age: Optional[int] = None
    is_admin: bool = False

class UserCreate(BaseModel):
    email: str
    password: str
    display_name: str
    full_name: str
    age: Optional[int] = None

class UserResponse(BaseModel):
    email: str
    display_name: str

    model_config = {
        "from_attributes": True
    }
