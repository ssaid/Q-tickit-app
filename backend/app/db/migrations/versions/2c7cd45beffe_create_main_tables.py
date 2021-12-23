"""create_main_tables

Revision ID: 2c7cd45beffe
Revises: 
Create Date: 2021-11-18 14:41:17.134833

"""
from alembic import op
import sqlalchemy as sa

from app.db.migrations.models.event import create_event_table

from app.db.migrations.models.link import create_link_table
from app.db.migrations.models.organization import create_organization_table
from app.db.migrations.models.organization_client import create_organization_client_table
from app.db.migrations.models.role import create_role_table
from app.db.migrations.models.state import create_state_table
from app.db.migrations.models.ticket import create_ticket_table
from app.db.migrations.models.client import create_client_table


# revision identifiers, used by Alembic
revision = '2c7cd45beffe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    create_client_table()
    create_organization_table()
    create_role_table()
    create_state_table()
    create_event_table()
    create_link_table()
    create_organization_client_table()
    create_ticket_table()


def downgrade() -> None:
    op.drop_table('ticket')
    op.drop_table('state')
    op.drop_table('role')
    op.drop_table('client')
    op.drop_table('organization_user')
    op.drop_table('organization')
    op.drop_table('link')
    op.drop_table('event')
