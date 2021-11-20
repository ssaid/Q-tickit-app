from alembic import op
import sqlalchemy as sa


def create_ticket_table() -> None:
    op.create_table(
        'ticket',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('customer', sa.String(255), nullable=False),
        sa.Column('customer_dni', sa.String(255), nullable=False),
        sa.Column('customer_email', sa.String(255), nullable=False),
        sa.Column('customer_adress', sa.String(255), nullable=False),
        sa.Column('customer_phone', sa.String(255), nullable=True),
        #relationships
        sa.Column('link_id', sa.Integer, sa.ForeignKey("link.id")),
        sa.Column('state_id', sa.Integer, sa.ForeignKey("state.id")),

    )