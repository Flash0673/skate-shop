from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, MetaData
from sqlalchemy.orm import relationship

from .database import Base


class Deck(Base):
    __tablename__ = "decks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    size = Column(Float(4, 2), index=True)
    description = Column(String, index=True)
    price = Column(Float(10,2), index=True)
    color = Column(String, index=True)
