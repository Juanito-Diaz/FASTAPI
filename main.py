from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional
from fastapi import FastAPI, Body

app = FastAPI(
    title="Aprendiendo FASTAPI",
    description="Una API en los primeros pasos",
    version="0.0.1",
)


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default='Titulo de la película', min_length=15, max_length=60)
    overview: str = Field(default='Descripción de la película', min_length=15, max_length=100)
    year: int = Field(default=2023)
    rating: float = Field(ge=1.0, le=10.0)
    category: str = Field(default='Categoría de la película', min_length=5, max_length=50)

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres de apariencia humanoide que tienen su propia cultura y lengua.",
        "year": 2009,
        "rating": 7.8,
        "category": "Acción"
    },

     {
            "id": 2,
            "title": "SING 2",
            "overview": "Son animales que viven en un mundo de música y baile.",
            "year": 2021,
            "rating": 7.1,
            "category": "Animación"
        }
]

@app.get("/", tags=["Inicio"])
def read_root():
    return HTMLResponse('<h2>Hola Mundo</h2>')

@app.get("/movies", tags=["Movies"])
def get_movies():
    return movies

@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int = Path(ge=1, le=100)):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return {"error": "Movie no encontrada"}


@app.get("/movies/", tags=["Movies"])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    return category


@app.post("/movies", tags=["Movies"])
def create_movie(movie: Movie):
    movies.append(movie.dict())
    print(movies)
    return movies

"""
def create_movie(
    id: int = Body(),
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body()
):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    print(movies)
    return title
"""

@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
            return movie

@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies

"""
def update_movie(
    id: int,
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body()
):
    for movie in movies:
        if movie["id"] == id:
            movie["title"] = title
            movie["overview"] = overview
            movie["year"] = year
            movie["rating"] = rating
            movie["category"] = category
            return movie
    return {"error": "Movie no encontrada"}

@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies
"""