import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.db import crud, models, schemas
from app.db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=['*'],
    allow_origins=["http://localhost","http://127.0.0.1:3000", 'http://localhost:8080', "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# TODO: Рефактор кода
@app.get("/decks/", response_model=list[schemas.Deck])
def read_decks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    decks = crud.get_decks(db, skip=skip, limit=limit)
    return decks


@app.get("/decks/{deck_id}", response_model=schemas.Deck)
def read_decks(deck_id: int, db: Session = Depends(get_db)):
    deck = crud.get_deck(db, deck_id)
    if deck is None:
        raise HTTPException(status_code=404, detail="Deck not found")  # TODO: Вынести в crud
    return deck


@app.post("/decks", response_model=schemas.Deck)
def create_deck(
        deck: schemas.DeckCreate, db: Session = Depends(get_db)
):
    return crud.create_deck(db=db, deck=deck)


@app.put("/decks/{deck_id}", response_model=schemas.Deck)
def update_deck(
        deck_id: int,
        deck: schemas.DeckEdit,
        db: Session = Depends(get_db)
):
    return crud.edit_deck(db=db, deck_id=deck_id, deck=deck)


@app.delete("/decks/{deck_id}", response_model=schemas.Deck)
def delete_deck(deck_id: int, db: Session = Depends(get_db)):
    return crud.delete_deck(db=db, deck_id=deck_id)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
