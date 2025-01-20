from pydantic import BaseModel
from pydantic import Field


class BaseCar(BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int = Field(..., ge=1960)
    cijena: float = Field(..., gt=0)
    boja: str


class Car(BaseCar):
    id: int


class CarWithPDV(Car):
    cijena_pdv: float
