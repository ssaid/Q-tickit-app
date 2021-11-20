from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from alembic import op
import sqlalchemy as sa


def create_user_table() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('login', sa.String, unique=True, index=True),
        sa.Column('name', sa.String),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('password', sa.String),
        sa.Column('commission', sa.Float),
        sa.Column('is_active', sa.Boolean, default=True),
    )
