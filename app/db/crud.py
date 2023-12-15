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
