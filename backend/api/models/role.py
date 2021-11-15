from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..config.database import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)
    #relationships
    organization_users = relationship("OrganizationUser", back_populates="role")