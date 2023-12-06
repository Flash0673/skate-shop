from pydantic import BaseModel


class DeckBase(BaseModel):
    title: str
    size: float
    price: float
    description: str | None = None


class DeckCreate(DeckBase):
    pass


class Deck(DeckBase):

    class Config:
        orm_mode = True
