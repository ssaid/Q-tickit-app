from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float

from alembic import op
import sqlalchemy as sa


def create_link_table() -> None:
    
    op.create_table(
        'link',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('max_tickets', sa.Integer),
        sa.Column('tickets_sold', sa.Integer),
        sa.Column('ticket_price', sa.Float),
        #relationships,
        sa.Column('event_id', sa.Integer, ForeignKey("event.id")),
    )