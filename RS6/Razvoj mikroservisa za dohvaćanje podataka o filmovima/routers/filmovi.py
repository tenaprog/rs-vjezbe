from typing import List, Literal, Optional
from fastapi import APIRouter, HTTPException, Query
from models.film import Film
from utils import parse_year_range, year_in_range
import requests

router_filmovi = APIRouter()

filmovi: List[Film] = []


def dohvati_filmove():
    url = "https://gist.githubusercontent.com/saniyusuf/406b843afdfb9c6a86e25753fe2761f4/raw/523c324c7fcc36efab8224f9ebb7556c09b69a14/Film.JSON"
    response = requests.get(url)
    global filmovi
    filmovi = [Film(**film) for film in response.json()]


dohvati_filmove()


@router_filmovi.get("/films", response_model=List[Film])
def get_films(
    min_year: Optional[str] = Query(None),
    max_year: Optional[str] = Query(None),
    min_rating: Optional[float] = Query(None, ge=0, le=10),
    max_rating: Optional[float] = Query(None, ge=0, le=10),
    type: Optional[Literal['movie', 'series']] = Query(None)
):
    filtrirani_filmovi = filmovi

    if min_year or max_year:
        start_year, end_year = None, None
        if min_year:
            start_year, _ = parse_year_range(min_year)
        if max_year:
            _, end_year = parse_year_range(max_year)

        filtrirani_filmovi = [
            film for film in filtrirani_filmovi if year_in_range(film.Year, start_year, end_year)
        ]

    if min_rating:
        filtrirani_filmovi = [
            film for film in filtrirani_filmovi if (film.imdbRating or 0) >= min_rating
        ]
    if max_rating:
        filtrirani_filmovi = [
            film for film in filtrirani_filmovi if (film.imdbRating or 0) <= max_rating
        ]

    if type:
        filtrirani_filmovi = [
            film for film in filtrirani_filmovi if film.Type == type
        ]

    return filtrirani_filmovi


@router_filmovi.get("/film/{imdbID}", response_model=Film)
def get_film_by_imdbID(imdbID: str):
    for film in filmovi:
        if film.imdbID == imdbID:
            return film
    raise HTTPException(status_code=404, detail="Film nije pronađen")


@router_filmovi.get("/film/search/{title}", response_model=Film)
def get_film_by_title(title: str):
    for film in filmovi:
        if film.Title.lower() == title.lower():
            return film
    raise HTTPException(status_code=404, detail="Film nije pronađen")
