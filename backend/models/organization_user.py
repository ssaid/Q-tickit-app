from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..config import Base


class OrganizationUser(Base):
    __tablename__ = "organization_user"

    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    organization = relationship("Organization", back_populates="organization_users")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="organization_users")
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="organization_users")