from pydantic import BaseModel, Field


class ObjavaBase(BaseModel):
    korisnik: str = Field(..., max_length=20)
    tekst: str = Field(..., max_length=280)
