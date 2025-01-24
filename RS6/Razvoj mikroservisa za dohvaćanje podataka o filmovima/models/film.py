from typing import List, Literal, Optional
from pydantic import BaseModel, Field
from .actor import Actor
from .writer import Writer


class Film(BaseModel):
    Title: str
    Year: str = Field(...)
    Rated: str
    Released: Optional[str] = None
    Runtime: str
    Genre: str
    Director: Optional[str] = None
    Writer: str
    Actors: str
    Plot: str
    Language: str
    Country: str
    Awards: Optional[str] = None
    Poster: Optional[str] = None
    Metascore: Optional[str] = None
    imdbRating: Optional[str] = None
    imdbVotes: Optional[str] = None
    imdbID: Optional[str] = None
    Type: Optional[Literal['movie', 'series']] = None
    Response: Optional[bool] = None
    Images: List[str] = Field(...)
