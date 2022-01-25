from typing import Optional, TYPE_CHECKING, List
from sqlmodel import SQLModel, Field, Relationship, Column, DateTime
from datetime import datetime


class Event(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    start_date: datetime = Field(sa_column=Column(DateTime(timezone=True)))
    end_date: datetime = Field(sa_column=Column(DateTime(timezone=True)))
    is_active: bool
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True)))

    #Relationships
    if TYPE_CHECKING:
        from .client import Client
        from .link import Link
        from .organization import Organization

    #m2o
    client_id: int = Field(default=None, foreign_key='client.id')
    client: 'Client' = Relationship(back_populates='events')

    organization_id: int = Field(default=None, foreign_key='organization.id')
    organization: 'Organization' = Relationship(back_populates='events')

    #o2m
    links: List['Link'] = Relationship(back_populates='event')


