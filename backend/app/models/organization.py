from typing import Optional, TYPE_CHECKING, List
from sqlmodel import SQLModel, Field, Relationship

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

    #Relationships
    if TYPE_CHECKING:
        from .event import Event
        from .organization_client_link import OrganizationClientLink

    #o2m
    events: List['Event'] = Relationship(back_populates='organization')

    #m2m
    clients: List['OrganizationClientLink'] = Relationship(back_populates='organizations')
