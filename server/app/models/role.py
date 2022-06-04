from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


    if TYPE_CHECKING:
        from .user import User
        from .organization_user_link import OrganizationUserLink


    users: List['OrganizationUserLink'] = Relationship(back_populates='role')


