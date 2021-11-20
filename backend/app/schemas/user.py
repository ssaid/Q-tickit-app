from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    email: str
    login: str
    name: str
    email: str
    commission: Optional[float] = 5.0
    is_active: Optional[bool]

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
