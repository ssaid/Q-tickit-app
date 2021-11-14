from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base


class OrganizationUser(Base):
    __tablename__ = "organization_user"

    id = Column(Integer, primary_key=True, index=True)
    #relationships
    organization_id = Column(Integer, ForeignKey("organization.id"))
    organizations = relationship("Organization", back_populates="organization_users")
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="organization_users")
    role_id = Column(Integer, ForeignKey("role.id"))
    role = relationship("Role", back_populates="organization_users")