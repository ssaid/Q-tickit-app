from pydantic import BaseModel
from typing import Optional
from .core import CoreModel, IDModelMixin


class UserBase(CoreModel):
    login: str
    name: str
    email: str
    commission: Optional[float] = 5.0
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str


class UserInDB(IDModelMixin, UserBase):
    pass