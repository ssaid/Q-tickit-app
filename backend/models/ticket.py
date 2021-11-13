from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..config import Base


class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, index=True)
    customer = Column(String(255), nullable=False)
    customer_dni = Column(String(255), nullable=False)
    customer_email = Column(String(255), nullable=False)
    customer_adress = Column(String(255), nullable=False)
    customer_phone = Column(String(255), nullable=True)
    link_id = Column(Integer, ForeignKey("link.id"))
    link = relationship("Link", back_populates="tickets")
    state_id = Column(Integer, ForeignKey("state.id"))
    state = relationship("State", back_populates="tickets")