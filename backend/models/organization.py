from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base

from . import event, organization_user


class Organization(Base):
    __tablename__ = "organization"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    adress = Column(String(255), nullable=False)
    #relationships
    events = relationship("Event", back_populates="organization")
    organization_users = relationship("OrganizationUser", back_populates="organization")
