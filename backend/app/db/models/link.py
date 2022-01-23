from typing import Optional
from sqlmodel import SQLModel, Field

class Link(SQLModel):
    id: int
    max_tickets: int
    tickets_sold: int
    ticket_price: float
    url: str


    # Relationships
    event_id: int

