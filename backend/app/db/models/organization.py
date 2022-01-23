from typing import Optional
from sqlmodel import SQLModel, Field

class Organization(SQLModel, table=True):
    id: Optional[int] = Field(int, primary_key=True, index=True)
    name: str
    city: Optional[str] = None
    state: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    # logo: Optional[bytes] = None
    is_active: Optional[bool] = True
    website: Optional[str] = None
