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

@app.get("/wheels", response_model=list[schemas.Wheels], tags=["wheels"])
def read_wheels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    wheels = crud.get_wheels(db, skip=skip, limit=limit)
    return wheels


@app.get("/wheels/{wheels_id}", response_model=schemas.Wheels, tags=["wheels"])
def read_wheel(wheels_id: int, db: Session = Depends(get_db)):
    wheel = crud.get_wheel(db, wheels_id)
    if wheel is None:
        raise HTTPException(status_code=404, detail="Wheels not found")  # TODO: Вынести в crud
    return wheel


@app.post("/wheels", response_model=schemas.Wheels, tags=["wheels"])
def create_complete(
        wheels: schemas.WheelsCreate, db: Session = Depends(get_db)
):
    return crud.create_wheels(db=db, wheels=wheels)


@app.put("/wheels/{wheels_id}", response_model=schemas.Wheels, tags=["wheels"])
def update_truck(
        wheels_id: int,
        wheels: schemas.WheelsEdit,
        db: Session = Depends(get_db)
):
    return crud.edit_wheels(db=db, wheels_id=wheels_id, wheels=wheels)


@app.delete("/wheels/{wheels_id}", response_model=schemas.Wheels, tags=["wheels"])
def delete_wheels(wheels_id: int, db: Session = Depends(get_db)):
    return crud.delete_wheels(db=db, wheels_id=wheels_id)


############------GRIP-TAPES------############

@app.get("/griptapes", response_model=list[schemas.Griptape], tags=["griptapes"])
def read_griptapes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    griptapes = crud.get_griptapes(db, skip=skip, limit=limit)
    return griptapes


@app.get("/griptapes/{griptape_id}", response_model=schemas.Griptape, tags=["griptapes"])
def read_griptape(griptape_id: int, db: Session = Depends(get_db)):
    griptape = crud.get_griptape(db, griptape_id)
    if griptape is None:
        raise HTTPException(status_code=404, detail="Wheels not found")  # TODO: Вынести в crud
    return griptape


@app.post("/griptapes", response_model=schemas.Griptape, tags=["griptapes"])
def create_griptape(
        griptape: schemas.GriptapeCreate, db: Session = Depends(get_db)
):
    return crud.create_griptape(db=db, griptape=griptape)


@app.put("/griptapes/{griptape_id}", response_model=schemas.Griptape, tags=["griptapes"])
def update_griptape(
        griptape_id: int,
        griptape: schemas.GriptapeEdit,
        db: Session = Depends(get_db)
):
    return crud.edit_griptape(db=db, griptape_id=griptape_id, griptape=griptape)


@app.delete("/griptapes/{griptape_id}", response_model=schemas.Griptape, tags=["griptapes"])
def delete_griptapes(griptape_id: int, db: Session = Depends(get_db)):
    return crud.delete_griptape(db=db, griptape_id=griptape_id)


############------BEARINGS------############


@app.get("/bearings", response_model=list[schemas.Bearings], tags=["bearings"])
def read_bearings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bearings = crud.get_bearings(db, skip=skip, limit=limit)
    return bearings


@app.get("/bearings/{bearings_id}", response_model=schemas.Bearings, tags=["bearings"])
def read_bearing(bearings_id: int, db: Session = Depends(get_db)):
    bearing = crud.get_bearing(db, bearings_id)
    if bearing is None:
        raise HTTPException(status_code=404, detail="Bearing not found")  # TODO: Вынести в crud
    return bearing


@app.post("/bearings", response_model=schemas.Bearings, tags=["bearings"])
def create_bearings(
        bearings: schemas.BearingsCreate, db: Session = Depends(get_db)
):
    return crud.create_bearings(db=db, bearings=bearings)


@app.put("/bearings/{bearings_id}", response_model=schemas.Bearings, tags=["bearings"])
def update_bearings(
        bearings_id: int,
        bearings: schemas.BearingsEdit,
        db: Session = Depends(get_db)
):
    return crud.edit_bearings(db=db, bearings_id=bearings_id, bearings=bearings)


@app.delete("/bearings/{bearings_id}", response_model=schemas.Bearings, tags=["bearings"])
def delete_wheels(bearings_id: int, db: Session = Depends(get_db)):
    return crud.delete_bearings(db=db, bearings_id=bearings_id)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
