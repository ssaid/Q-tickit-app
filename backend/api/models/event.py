from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..config.database import Base
from . import organization


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(500), nullable=False)
    #relationship
    organization_id = Column(Integer, ForeignKey("organization.id"))
    organization = relationship("Organization", back_populates="events")
    links = relationship("Link", back_populates="event")
