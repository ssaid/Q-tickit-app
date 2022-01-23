from typing import Optional
from sqlmodel import SQLModel, Field


class Event(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    start_date: str     # TODO: Change to datetime
    end_date: str       # TODO: Change to datetime
    is_active: bool
    created_at: str     # TODO: Change to datetime
    updated_at: str     # TODO: Change to datetime

    #Relationships

    created_by: int     # foreign key a user
    updated_by: int     # foreign key a user
    organization_id: int        # foreign key a organization


