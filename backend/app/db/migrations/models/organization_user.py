from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from alembic import op
import sqlalchemy as sa

def create_organization_user_table() -> None:
    op.create_table(
        'organization_user',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        #relationships
        sa.Column('organization_id', sa.Integer, ForeignKey("organization.id")),
        sa.Column('user_id', sa.Integer, ForeignKey("user.id")),
        sa.Column('role_id', sa.Integer, ForeignKey("role.id"))
    )
