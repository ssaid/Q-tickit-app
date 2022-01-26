from typing import Optional, List, TYPE_CHECKING, ForwardRef
from sqlmodel import SQLModel, Field, Relationship



class UserBase(SQLModel):
    name: str
    login: str
    email: str
    is_active: Optional[bool] = True
    commission: Optional[float] = 5.0

class UserRead(UserBase):
    id: int

class UserCreate(UserBase):
    password: str


class User(UserCreate, table=True):
    __tablename__ = 'users'

    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    # Relationships
    if TYPE_CHECKING:
        from .event import Event
        from .organization_user_link import OrganizationUserLink

    #o2m
    events: List['Event'] = Relationship(back_populates='user')

    #m2m
    organizations: List['OrganizationUserLink'] = Relationship(back_populates='user')


class UserReadWithRelationships(UserRead):
    # Relationships
    if TYPE_CHECKING:
        from .event import Event
        from .organization_user_link import OrganizationUserLink

    #o2m
    events: List['Event'] = []

    #m2m
    organizations: List['OrganizationUserLink'] = []



class UserCommission(SQLModel):
    id: int
    commission: float

class UserIsActive(SQLModel):
    id: int
    is_active: bool


