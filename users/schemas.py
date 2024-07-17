from pydantic import BaseModel, EmailStr
from typing import List

class UserBase(BaseModel):
    username: str
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None
    country: str | None = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    roles: List[str]

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str
