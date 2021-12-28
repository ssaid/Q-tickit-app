from pydantic import BaseModel
from typing import Optional
from .core import CoreModel, IDModelMixin


class ClientBase(CoreModel):
    login: str
    name: str
    email: str
    commission: Optional[float] = 5.0
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True

class ClientCreate(ClientBase):
    password: str


class ClientInDB(IDModelMixin, ClientBase):
    pass
