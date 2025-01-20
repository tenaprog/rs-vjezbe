from typing import List, TypedDict
from pydantic import BaseModel, Field


class StolInfo(TypedDict):
    broj: int
    lokacija: str


class Jelo(BaseModel):
    id: int
    naziv: str
    cijena: float = Field(..., gt=0)


class RestaurantOrder(BaseModel):
    id: int
    ime_kupca: str
    stol_info: StolInfo
    jela: List[Jelo]
    ukupna_cijena: float = Field(..., gt=0)
