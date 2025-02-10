from pydantic import BaseModel


class LoginBase(BaseModel):
    korisnik: str
    lozinka: str
