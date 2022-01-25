from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


    if TYPE_CHECKING:
        from .client import client
        from .organization_client_link import organization_client_link


    clients: List['OrganizationClientLink'] = Relationship(back_populates='role')


