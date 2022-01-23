from typing import Optional
from sqlmodel import SQLModel, Field

class OrganizationClient(SQLModel, table=True):
    """
    OrganizationClient model
    """
    id: int = Field(default=None, primary_key=True)
    organization_id: int = Field(int)
    client_id: int
    role_id: int
