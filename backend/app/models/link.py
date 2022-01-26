from typing import Optional, TYPE_CHECKING, List
from sqlmodel import SQLModel, Field, Relationship

class Link(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    max_tickets: int
    tickets_sold: int
    ticket_price: float
    url: str


    # Relationships
    if TYPE_CHECKING:
        from .event import Event
        from .ticket import Ticket

    event_id: int = Field(default=None, foreign_key='event.id')
    event: 'Event' = Relationship(back_populates='links')

    tickets: List['Ticket'] = Relationship(back_populates='ticket_link')
