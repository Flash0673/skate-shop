from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas


############------DECKS------############

def get_deck(db: Session, deck_id: int):
    return db.query(models.Deck).filter(models.Deck.id == deck_id).first()


def get_decks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Deck).offset(skip).limit(limit).all()


def create_deck(db: Session, deck: schemas.DeckCreate):
    db_deck = models.Deck(title=deck.title, size=deck.size, price=deck.price, description=deck.description)
    db.add(db_deck)
    db.commit()
    db.refresh(db_deck)
    return db_deck


def delete_deck(db: Session, deck_id: int):
    deck = get_deck(db, deck_id)
    if not deck:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Deck not found")
    db.delete(deck)
    db.commit()
    return deck


def edit_deck(
        db: Session, deck_id: int, deck: schemas.DeckEdit
) -> schemas.Deck:
    db_deck = get_deck(db, deck_id)
    if not db_deck:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Deck not found")
    update_data = deck.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_deck, key, value)

    db.add(db_deck)
    db.commit()
    db.refresh(db_deck)
    return db_deck


############------TRUCKS------############


def get_truck(db: Session, truck_id: int):
    return db.query(models.Truck).filter(models.Truck.id == truck_id).first()


def get_trucks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Truck).offset(skip).limit(limit).all()


def create_truck(db: Session, truck: schemas.TruckCreate):
    db_truck = models.Truck(
        title=truck.title,
        size=truck.size,
        price=truck.price,
        description=truck.description,
        quantity=truck.quantity,
        has_bushing=truck.has_bushing
    )
    db.add(db_truck)
    db.commit()
    db.refresh(db_truck)
    return db_truck


def delete_truck(db: Session, truck_id: int):
    truck = get_truck(db, truck_id)
    if not truck:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Truck not found")
    db.delete(truck)
    db.commit()
    return truck


def edit_truck(
        db: Session, truck_id: int, truck: schemas.TruckEdit
) -> schemas.Truck:
    db_truck = get_truck(db, truck_id)
    if not db_truck:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Truck not found")
    update_data = truck.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_truck, key, value)

    db.add(db_truck)
    db.commit()
    db.refresh(db_truck)
    return db_truck


############------COMPLETES------############

def get_complete(db: Session, complete_id: int):
    return db.query(models.Complete).filter(models.Complete.id == complete_id).first()


def get_completes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Complete).offset(skip).limit(limit).all()


def create_complete(db: Session, complete: schemas.CompleteCreate):
    db_complete = models.Complete(
        title=complete.title,
        size=complete.size,
        price=complete.price,
        description=complete.description,
    )
    db.add(db_complete)
    db.commit()
    db.refresh(db_complete)
    return db_complete


def delete_complete(db: Session, complete_id: int):
    complete = get_complete(db, complete_id)
    if not complete:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Complete not found")
    db.delete(complete)
    db.commit()
    return complete


def edit_complete(
        db: Session, complete_id: int, complete: schemas.CompleteEdit
) -> schemas.Complete:
    db_complete = get_complete(db, complete_id)
    if not db_complete:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Complete not found")
    update_data = complete.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_complete, key, value)

    db.add(db_complete)
    db.commit()
    db.refresh(db_complete)
    return db_complete


############------WHEELS------############


def get_wheel(db: Session, wheels_id: int):
    return db.query(models.Wheels).filter(models.Wheels.id == wheels_id).first()


def get_wheels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Wheels).offset(skip).limit(limit).all()


def create_wheels(db: Session, wheels: schemas.WheelsCreate):
    db_wheels = models.Wheels(
        title=wheels.title,
        size=wheels.size,
        price=wheels.price,
        description=wheels.description,
        color=wheels.color,
        hardness=wheels.hardness
    )
    db.add(db_wheels)
    db.commit()
    db.refresh(db_wheels)
    return db_wheels


def delete_wheels(db: Session, wheels_id: int):
    wheels = get_wheel(db, wheels_id)
    if not wheels:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Wheels not found")
    db.delete(wheels)
    db.commit()
    return wheels


def edit_wheels(
        db: Session, wheels_id: int, wheels: schemas.WheelsEdit
) -> schemas.Wheels:
    db_wheels = get_wheel(db, wheels_id)
    if not db_wheels:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Wheels not found")
    update_data = wheels.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_wheels, key, value)

    db.add(db_wheels)
    db.commit()
    db.refresh(db_wheels)
    return db_wheels


############------GRIP-TAPES------############


def get_griptape(db: Session, griptape_id: int):
    return db.query(models.Griptape).filter(models.Griptape.id == griptape_id).first()


def get_griptapes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Griptape).offset(skip).limit(limit).all()


def create_griptape(db: Session, griptape: schemas.GriptapeCreate):
    db_griptape = models.Griptape(
        title=griptape.title,
        price=griptape.price,
        description=griptape.description,
        length=griptape.length,
        width=griptape.width
    )
    db.add(db_griptape)
    db.commit()
    db.refresh(db_griptape)
    return db_griptape


def delete_griptape(db: Session, griptape_id: int):
    griptape = get_griptape(db, griptape_id)
    if not griptape:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Grip-Tape not found")
    db.delete(griptape)
    db.commit()
    return griptape


def edit_griptape(
        db: Session, griptape_id: int, griptape: schemas.GriptapeEdit
) -> schemas.Griptape:
    db_griptape = get_griptape(db, griptape_id)
    if not db_griptape:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Grip-Tape not found")
    update_data = griptape.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_griptape, key, value)

    db.add(db_griptape)
    db.commit()
    db.refresh(db_griptape)
    return db_griptape


############------BEARINGS------############


def get_bearing(db: Session, bearing_id: int):
    return db.query(models.Bearing).filter(models.Bearing.id == bearing_id).first()


def get_bearings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Bearing).offset(skip).limit(limit).all()


def create_bearings(db: Session, bearings: schemas.BearingsCreate):
    db_bearings = models.Bearing(
        title=bearings.title,
        price=bearings.price,
        description=bearings.description,
    )
    db.add(db_bearings)
    db.commit()
    db.refresh(db_bearings)
    return db_bearings


def delete_bearings(db: Session, bearings_id: int):
    bearings = get_bearing(db, bearings_id)
    if not bearings:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Bearings not found")
    db.delete(bearings)
    db.commit()
    return bearings


def edit_bearings(
        db: Session, bearings_id: int, bearings: schemas.CompleteEdit
) -> schemas.Bearings:
    db_bearings = get_bearing(db, bearings_id)
    if not db_bearings:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Bearings not found")
    update_data = bearings.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_bearings, key, value)

    db.add(db_bearings)
    db.commit()
    db.refresh(db_bearings)
    return db_bearings
