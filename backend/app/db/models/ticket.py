from typing import Optional
from sqlmodel import SQLModel, Field

class Ticket(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    customer: str
    customer_dni: str
    customer_email: str
    customer_phone: str
    customer_address: str


    #Relationships

    #link_id: int
    #state_id: int
