from alembic import op
import sqlalchemy as sa


def create_role_table() -> None:
    op.create_table(
        'role',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(255), nullable=False),
    )