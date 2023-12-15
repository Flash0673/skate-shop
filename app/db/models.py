from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, MetaData
from sqlalchemy.orm import relationship

from .database import Base


class Deck(Base):
    __tablename__ = "decks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    size = Column(Float(4, 2), index=True)
    description = Column(String)
    price = Column(Float(10, 2), index=True)
    color = Column(String, index=True)


class Truck(Base):
    __tablename__ = "trucks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    size = Column(Float(4, 2), index=True)
    description = Column(String)
    price = Column(Float(10, 2), index=True)
    color = Column(String, index=True)
    quantity = Column(Integer)
    has_bushing = Column(Boolean)


class Complete(Base):
    __tablename__ = "completes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    size = Column(Float(4, 2), index=True)
    description = Column(String)
    price = Column(Float(10, 2), index=True)
    # TODO: Добавить ForeignKey на составные части


class Wheels(Base):
    __tablename__ = "wheels"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    size = Column(Float(4, 2), index=True)
    description = Column(String)
    price = Column(Float(10, 2), index=True)
    color = Column(String, index=True)
    hardness = Column(String, index=True)


class Griptape(Base):
    __tablename__ = "griptapes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float(10, 2), index=True)
    length = Column(Float(5, 2))
    width = Column(Float(5, 2))


class Bearing(Base):
    __tablename__ = "bearings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float(10, 2), index=True)
