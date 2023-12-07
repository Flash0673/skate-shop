from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas


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
