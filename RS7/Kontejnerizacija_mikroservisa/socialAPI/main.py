from fastapi import FastAPI, HTTPException
from typing import List
from datetime import datetime

from models.Objava import Objava
from models.ObjavaBase import ObjavaBase

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


@app.get("/korisnici/{korisnik}/objave", response_model=List[Objava])
def dohvati_objave_korisnika(korisnik: str):
    korisnikove_objave = [
        objava for objava in objave_db if objava.korisnik == korisnik]
    return korisnikove_objave
