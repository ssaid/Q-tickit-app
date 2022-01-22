from pydantic import BaseModel
from typing import Optional, List
from .core import CoreModel, IDModelMixin
from .organization import ClientOnOrganization


class ClientBase(CoreModel):
    login: str
    name: str
    email: str
    commission: Optional[float] = 5.0
    is_active: Optional[bool] = True
    organizations: List[ClientOnOrganization] = []

    class Config:
        orm_mode = True

class ClientCreate(ClientBase):
    password: str

class PasswordUpdate(BaseModel):
    new_password: str
    old_password: str

class CommissionUpdate(BaseModel):
    commission: float

class StatusUpdate(BaseModel):
    is_active: bool

class ClientInDB(IDModelMixin, ClientBase):
    pass
