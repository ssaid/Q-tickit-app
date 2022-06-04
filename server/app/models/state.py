from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

class State(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    if TYPE_CHECKING:
        from .ticket import Ticket

    tickets: List['Ticket'] = Relationship(back_populates='state')
