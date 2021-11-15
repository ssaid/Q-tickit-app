from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    login: str
    name: str
    password: str
    commission: float
    email: str
    is_active: Optional[bool] = True


class ShowUser(BaseModel):
    login: str
    name: str
    email: str