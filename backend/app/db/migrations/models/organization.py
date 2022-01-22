from alembic import op
import sqlalchemy as sa

def create_organization_table() -> None:
    op.create_table(
        'organization',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('city', sa.String(255), nullable=False),
        sa.Column('state', sa.String(255), nullable=False),
        sa.Column('address', sa.String(255), nullable=False),
        sa.Column('phone', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('logo', sa.Binary, nullable=False),
        sa.Column('is_active', sa.Boolean, nullable=False),
        sa.Column('website', sa.String(255), nullable=False),
    )
