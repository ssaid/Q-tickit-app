from alembic import op
import sqlalchemy as sa


def create_state_table() -> None:
    op.create_table(
        'state',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(255), nullable=False),
    )