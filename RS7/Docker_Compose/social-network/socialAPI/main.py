from fastapi import FastAPI, HTTPException
import requests
from typing import List
from datetime import datetime

from models.Objava import Objava
from models.ObjavaBase import ObjavaBase
from models.loginBase import LoginBase

app = FastAPI()

objave_db: List[Objava] = []
next_id = 1


@app.post("/objava", response_model=Objava)
def dodaj_objavu(objava: ObjavaBase):
    global next_id

    nova_objava = Objava(
        id=next_id,
        korisnik=objava.korisnik,
        tekst=objava.tekst,
        vrijeme=datetime.utcnow()
    )
    objave_db.append(nova_objava)
    next_id += 1
    return nova_objava


@app.get("/objava/{id}", response_model=Objava)
def dohvati_objavu(id: int):
    for objava in objave_db:
        if objava.id == id:
            return objava
    raise HTTPException(status_code=404, detail="Objava nije pronađena")


@app.post("/korisnici/{korisnik}/objave", response_model=List[Objava])
def dohvati_objave_korisnika(request: LoginBase):

    auth_url = "http://authapi:9000/login"
    response = requests.post(auth_url, json=request.model_dump())

    if response.status_code != 200 or not response.json().get("autorizacija"):
        raise HTTPException(
            status_code=401, detail="Neispravni korisnički podaci")

    return [objava for objava in objave_db if objava.korisnik == request.korisnik]
