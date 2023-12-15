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


############------COMPLETES------############

class CompleteBase(BaseModel):
    title: str
    size: float
    price: float
    description: Union[str, None]


class CompleteCreate(CompleteBase):
    pass

    class Config:
        orm_mode = True


class Complete(CompleteBase):
    id: int

    class Config:
        orm_mode = True


class CompleteEdit(CompleteBase):
    class Config:
        orm_mode = True


############------WHEELS------############


class WheelsBase(BaseModel):
    title: str
    size: float
    price: float
    description: Union[str, None]
    color: str
    hardness: str


class WheelsCreate(WheelsBase):
    pass

    class Config:
        orm_mode = True


class Wheels(WheelsBase):
    id: int

    class Config:
        orm_mode = True


class WheelsEdit(WheelsBase):
    class Config:
        orm_mode = True


############------GRIP-TAPES------############


class GriptapeBase(BaseModel):
    title: str
    price: float
    description: Union[str, None]
    length: float
    width: float


class GriptapeCreate(GriptapeBase):
    pass

    class Config:
        orm_mode = True


class Griptape(GriptapeBase):
    id: int

    class Config:
        orm_mode = True


class GriptapeEdit(GriptapeBase):
    class Config:
        orm_mode = True


############------BEARINGS------############


class BearingsBase(BaseModel):
    title: str
    price: float
    description: Union[str, None]


class BearingsCreate(BearingsBase):
    pass

    class Config:
        orm_mode = True


class Bearings(BearingsBase):
    id: int

    class Config:
        orm_mode = True


class BearingsEdit(BearingsBase):
    class Config:
        orm_mode = True

