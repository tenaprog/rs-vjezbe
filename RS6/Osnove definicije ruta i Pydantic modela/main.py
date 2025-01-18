from fastapi import FastAPI
from models import CreateFilm, ResponseFilm


app = FastAPI()

filmovi = [
    {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
    {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
    {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
    {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008},
]

filmovi_validirani = [ResponseFilm(**film) for film in filmovi]

# zadatak_1, zadatak_2, zadatak_5


@app.get("/filmovi", response_model=list[ResponseFilm])
async def get_filmovi(genre: str = None, min_godina: int = 2000):
    toReturn = filmovi_validirani
    if genre:
        toReturn = [
            film for film in toReturn if film.genre.lower() == genre.lower()
        ]
    if min_godina:
        toReturn = [
            film for film in toReturn if film.godina >= min_godina
        ]
    return toReturn


# zadatak_3
@app.get("/filmovi/{id}", response_model=ResponseFilm)
async def get_film_by_id(id: int):
    for film in filmovi_validirani:
        if film.id == id:
            return film


# zadatak_4
@app.post("/filmovi")
async def get_film_by_id(film: CreateFilm):
    id = len(filmovi) + 1
    novi_film = CreateFilm(id=id, **film.model_dump())
    filmovi_validirani.append(novi_film)
    return novi_film
