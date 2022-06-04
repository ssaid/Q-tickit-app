from typing import Optional, TYPE_CHECKING, List
from sqlmodel import SQLModel, Field, Relationship, Column, DateTime
from datetime import datetime




#%% OrganizationUserLink

class OrganizationUserLink(SQLModel, table=True):

    id: int = Field(default=None, primary_key=True)

    organization_id: int = Field(default=None, foreign_key='organization.id', nullable=False)
    organization: 'Organization' = Relationship(back_populates='users')

    user_id: int = Field(default=None, foreign_key='users.id', nullable=False)
    user: 'User' = Relationship(back_populates='organizations')

    permissions: Optional[str] = "['camera','home']"

#%% User

class UserCredentials(SQLModel):
    login: str
    password: str

class UserAuthenticated(SQLModel):
    token: str
    expiration: datetime
    user_id: int

class UserBase(SQLModel):
    name: str
    login: str
    email: str
    is_active: Optional[bool] = True
    commission: Optional[float] = 5.0

class UserRead(UserBase):
    id: int

class UserReadInOrganization(SQLModel):
    id: int
    name: str
    is_active: bool
    permissions: str

class UserReadWithRelationships(UserRead):

    pass
    #o2m
    events: List['Event'] = []

    #m2m
    organizations: List['OrganizationUserLink'] = []

class UserCreate(UserBase):
    password: str

class UserValidation(UserCreate):
    id: int

class User(UserCreate, table=True):
    __tablename__ = 'users'

    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    # Relationships

    #o2m
    events: List['Event'] = Relationship(back_populates='user')

    #m2m
    organizations: List['OrganizationUserLink'] = Relationship(back_populates='user')


class UserCommission(SQLModel):
    id: int
    commission: float

class UserIsActive(SQLModel):
    id: int
    is_active: bool




#%% Event
class EventCreate(SQLModel):
    name: str
    description: str
    start_date: datetime = Field(sa_column=Column(DateTime(timezone=True)))
    end_date: datetime = Field(sa_column=Column(DateTime(timezone=True)))
    is_active: bool
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True)))

    #m2o
    user_id: int = Field(default=None, foreign_key='users.id')

    #TODO: quitar el optional
    organization_id: Optional[int] = Field(default=None, foreign_key='organization.id')


class Event(EventCreate, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)


    #m2o
    user: User = Relationship(back_populates='events')
    organization: 'Organization' = Relationship(back_populates='events')

    #o2m
    links: List['Link'] = Relationship(back_populates='event')


#%% Link


class Link(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    max_tickets: int
    tickets_sold: int
    ticket_price: float
    url: str



    event_id: int = Field(default=None, foreign_key='event.id')
    event: Event = Relationship(back_populates='links')

    tickets: List['Ticket'] = Relationship(back_populates='ticket_link')

#%% Organization

class OrganizationCreate(SQLModel):

    name: str
    city: Optional[str] = None
    state: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    # logo: Optional[bytes] = None
    is_active: Optional[bool] = True
    website: Optional[str] = None
    user_id: int

class OrganizationRead(OrganizationCreate):
    id: int

    users: List['UserReadInOrganization'] = []


class Organization(OrganizationCreate, table=True):

    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    #o2m
    events: List[Event] = Relationship(back_populates='organization')

    #m2m
    users: List['OrganizationUserLink'] = Relationship(back_populates='organization')


#%% State

class State(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


    tickets: List['Ticket'] = Relationship(back_populates='state')

#%% Tickets


class Ticket(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    customer: str
    customer_dni: str
    customer_email: str
    customer_phone: str
    customer_address: str


    state_id: int = Field(default=None, foreign_key='state.id')
    state: State = Relationship(back_populates='tickets')

    link_id: int = Field(default=None, foreign_key='link.id')
    ticket_link: Link = Relationship(back_populates='tickets')


UserBase.update_forward_refs()
UserRead.update_forward_refs()
UserReadWithRelationships.update_forward_refs()
UserCreate.update_forward_refs()
User.update_forward_refs()
UserCommission.update_forward_refs()
UserIsActive.update_forward_refs()
Event.update_forward_refs()
Link.update_forward_refs()
Organization.update_forward_refs()
OrganizationUserLink.update_forward_refs()
State.update_forward_refs()
Ticket.update_forward_refs()
OrganizationRead.update_forward_refs()
UserReadInOrganization.update_forward_refs()


