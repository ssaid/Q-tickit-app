from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

class OrganizationClientLink(SQLModel, table=True):

    id: int = Field(default=None, primary_key=True)

    if TYPE_CHECKING:
        from .organization import Organization
        from .client import Client
        from .role import Role

    organization_id: int = Field(default=None, foreign_key='organization.id')
    organization: 'Organization' = Relationship(back_populates='clients')

    client_id: int = Field(default=None, foreign_key='client.id')
    client: 'Client' = Relationship(back_populates='organizations')

    role_id: int = Field(default=None, foreign_key='role.id')
    role: 'Role' = Relationship(back_populates='clients')
