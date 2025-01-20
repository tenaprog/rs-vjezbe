from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from models import BaseCar, Car, CarWithPDV

app = FastAPI()

db = []


@app.get("/cars", response_model=List[Car])
def get_cars(
    min_cijena: Optional[float] = Query(None, gt=0),
    max_cijena: Optional[float] = Query(None, gt=0),
    min_godina: Optional[int] = Query(None, ge=1960),
    max_godina: Optional[int] = Query(None, ge=1960),
):
    if min_cijena and max_cijena and min_cijena > max_cijena:
        raise HTTPException(
            status_code=400, detail="Minimalna cijena ne smije biti veća od maksimalne cijene.")
    if min_godina and max_godina and min_godina > max_godina:
        raise HTTPException(
            status_code=400, detail="Minimalna godina proizvodnje ne smije biti veća od maksimalne godine proizvodnje.")

    filtered_cars = [
        car for car in db
        if (min_cijena is None or car["cijena"] >= min_cijena)
        and (max_cijena is None or car["cijena"] <= max_cijena)
        and (min_godina is None or car["godina_proizvodnje"] >= min_godina)
        and (max_godina is None or car["godina_proizvodnje"] <= max_godina)
    ]
    return filtered_cars


@app.get("/cars/{car_id}", response_model=Car)
def get_car(car_id: int):
    for car in db:
        if car["id"] == car_id:
            return car
    raise HTTPException(status_code=404, detail="Automobil nije pronađen.")


@app.post("/cars", response_model=CarWithPDV)
def add_car(car: BaseCar):
    if any(existing_car["marka"] == car.marka and existing_car["model"] == car.model for existing_car in db):
        raise HTTPException(
            status_code=400, detail="Automobil već postoji u bazi podataka.")

    new_id = len(db) + 1
    new_car = {
        **car.model_dump(),
        "id": new_id,
        "cijena_pdv": round(car.cijena*1.25, 2)
    }
    db.append(new_car)

    return new_car
