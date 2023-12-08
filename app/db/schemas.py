from pydantic import BaseModel
from typing import Union 



class DeckBase(BaseModel):
    title: str
    size: float
    price: float
    description: Union[str, None]


class DeckCreate(DeckBase):
    pass


class Deck(DeckBase):

    class Config:
        orm_mode = True
