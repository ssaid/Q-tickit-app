from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from ..config.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    commission = Column(Float)
    is_active = Column(Boolean, default=True)
    #relationships
    organization_users = relationship("OrganizationUser", back_populates="user")