from typing import Optional
from sqlmodel import SQLModel, Field



class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    login: str
    email: str
    password: str
    commission: float
    is_active: bool

