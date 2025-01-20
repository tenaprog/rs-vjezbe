from pydantic import BaseModel, Field
from datetime import datetime


class Izdavac(BaseModel):
    naziv: str
    adresa: str


class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godina_izdavanja: int = Field(
        default=datetime.now().year, ge=0)
    broj_stranica: int = Field(..., gt=0)
    izdavac: Izdavac
