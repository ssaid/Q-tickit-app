from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..config import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)
    organization_users = relationship("OrganizationUser", back_populates="role")