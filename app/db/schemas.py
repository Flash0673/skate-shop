from pydantic import BaseModel
from typing import Union


############------DECKS------############

class DeckBase(BaseModel):
    title: str
    size: float
    price: float
    description: Union[str, None]


class DeckCreate(DeckBase):
    pass

    class Config:
        orm_mode = True


class Deck(DeckBase):
    id: int

    class Config:
        orm_mode = True


class DeckEdit(DeckBase):
    class Config:
        orm_mode = True


############------TRUCKS------############


class TruckBase(BaseModel):
    title: str
    size: float
    price: float
    description: Union[str, None]
    quantity: int = 1
    has_bushing: bool = False


class Truck(TruckBase):
    id: int

    class Config:
        orm_mode = True


class TruckCreate(TruckBase):
    class Config:
        orm_mode = True


class TruckEdit(TruckBase):
    class Config:
        orm_mode = True
