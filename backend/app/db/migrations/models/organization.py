from alembic import op
import sqlalchemy as sa

def create_organization_table() -> None:
    op.create_table(
        'organization',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('city', sa.String(255), nullable=False),
        sa.Column('state', sa.String(255), nullable=False),
        sa.Column('adress', sa.String(255), nullable=False),
    )
