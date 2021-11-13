from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..config import Base


class State(Base):
    __tablename__ = "state"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)
    tickets = relationship("Tickets", back_populates="state")