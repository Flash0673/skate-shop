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
    allow_origins=["http://localhost", "http://127.0.0.1:3000", 'http://localhost:8080', "http://localhost:3000"],
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


############------DECKS------############

# TODO: Рефактор кода
@app.get("/decks", response_model=list[schemas.Deck], tags=["decks"])
def read_decks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    decks = crud.get_decks(db, skip=skip, limit=limit)
    return decks


@app.get("/decks/{deck_id}", response_model=schemas.Deck, tags=["decks"])
def read_decks(deck_id: int, db: Session = Depends(get_db)):
    deck = crud.get_deck(db, deck_id)
    if deck is None:
        raise HTTPException(status_code=404, detail="Deck not found")  # TODO: Вынести в crud
    return deck


@app.post("/decks", response_model=schemas.Deck, tags=["decks"])
def create_deck(
        deck: schemas.DeckCreate, db: Session = Depends(get_db)
):
    return crud.create_deck(db=db, deck=deck)


@app.put("/decks/{deck_id}", response_model=schemas.Deck, tags=["decks"])
def update_deck(
        deck_id: int,
        deck: schemas.DeckEdit,
        db: Session = Depends(get_db)
):
    return crud.edit_deck(db=db, deck_id=deck_id, deck=deck)


@app.delete("/decks/{deck_id}", response_model=schemas.Deck, tags=["decks"])
def delete_deck(deck_id: int, db: Session = Depends(get_db)):
    return crud.delete_deck(db=db, deck_id=deck_id)


############------TRUCKS------############

@app.get("/trucks", response_model=list[schemas.Truck], tags=["trucks"])
def read_trucks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    trucks = crud.get_trucks(db, skip=skip, limit=limit)
    return trucks


@app.get("/trucks/{truck_id}", response_model=schemas.Truck, tags=["trucks"])
def read_truck(truck_id: int, db: Session = Depends(get_db)):
    truck = crud.get_truck(db, truck_id)
    if truck is None:
        raise HTTPException(status_code=404, detail="Truck not found")  # TODO: Вынести в crud
    return truck


@app.post("/trucks", response_model=schemas.Truck, tags=["trucks"])
def create_truck(
        truck: schemas.TruckCreate, db: Session = Depends(get_db)
):
    return crud.create_truck(db=db, truck=truck)


@app.put("/trucks/{truck_id}", response_model=schemas.Truck, tags=["trucks"])
def update_truck(
        truck_id: int,
        truck: schemas.TruckEdit,
        db: Session = Depends(get_db)
):
    return crud.edit_truck(db=db, truck_id=truck_id, truck=truck)


@app.delete("/trucks/{truck_id}", response_model=schemas.Truck, tags=["trucks"])
def delete_truck(truck_id: int, db: Session = Depends(get_db)):
    return crud.delete_truck(db=db, truck_id=truck_id)


############------COMPLETES------############

@app.get("/completes", response_model=list[schemas.Complete], tags=["completes"])
def read_completes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    completes = crud.get_completes(db, skip=skip, limit=limit)
    return completes


@app.get("/completes/{complete_id}", response_model=schemas.Complete, tags=["completes"])
def read_complete(complete_id: int, db: Session = Depends(get_db)):
    complete = crud.get_complete(db, complete_id)
    if complete is None:
        raise HTTPException(status_code=404, detail="Complete not found")  # TODO: Вынести в crud
    return complete


@app.post("/completes", response_model=schemas.Complete, tags=["completes"])
def create_complete(
        complete: schemas.CompleteCreate, db: Session = Depends(get_db)
):
    return crud.create_complete(db=db, complete=complete)


@app.put("/completes/{complete_id}", response_model=schemas.Complete, tags=["completes"])
def update_truck(
        complete_id: int,
        complete: schemas.CompleteEdit,
        db: Session = Depends(get_db)
):
    return crud.edit_complete(db=db, complete_id=complete_id, complete=complete)


@app.delete("/completes/{complete_id}", response_model=schemas.Complete, tags=["completes"])
def delete_truck(complete_id: int, db: Session = Depends(get_db)):
    return crud.delete_complete(db=db, complete_id=complete_id)

############------WHEELS------############


############------GRIP-TAPES------############


############------BEARINGS------############


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
