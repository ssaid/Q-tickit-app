from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from . import event



class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    login: str
    email: str
    password: str
    commission: float
    is_active: bool

    # Relationships
    if TYPE_CHECKING:
        from .event import Event
        from .organization_client_link import OrganizationClientLink

    events: List['Event'] = Relationship(back_populates='client')

    #m2m
    organizations: List['OrganizationClientLink'] = Relationship(back_populates='clients')


