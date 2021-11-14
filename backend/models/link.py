from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float

from config.db import Base


class Link(Base):
    __tablename__ = "link"

    id = Column(Integer, primary_key=True, index=True)
    max_tickets = Column(Integer)
    tickets_sold = Column(Integer)
    ticket_price = Column(Float)
    #relationships
    tickets = relationship("Ticket", back_populates="links")
    event_id = Column(Integer, ForeignKey("event.id"))
    event = relationship("Events", back_populates="links")
