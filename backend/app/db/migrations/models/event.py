from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from alembic import op
import sqlalchemy as sa


def create_event_table() -> None:

    op.create_table(
        'event',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.String(length=255), nullable=False),
        sa.Column('start_date', sa.DateTime, nullable=False),
        sa.Column('end_date', sa.DateTime, nullable=False),
        sa.Column('is_active', sa.Boolean, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.Column('created_by', sa.Integer,
                  ForeignKey('client.id'), nullable=False),
        sa.Column('updated_by', sa.Integer,
                  ForeignKey('client.id'), nullable=False),
        sa.Column('organization_id', sa.Integer, ForeignKey(
            'organization.id'), nullable=False)
    )
