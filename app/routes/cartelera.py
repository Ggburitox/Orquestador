from fastapi import APIRouter
from typing import List
from app.service.cartelera_service import crear_pelicula, listar_peliculas, obtener_pelicula
from app.schemas.cartelera_schemas import PeliculaCreate, Pelicula

router = APIRouter(tags=["Cartelera"])

@router.post("/peliculas", response_model=Pelicula)
async def crear_pelicula_route(pelicula: PeliculaCreate):
    return await crear_pelicula(pelicula)

@router.get("/peliculas", response_model=List[Pelicula])
async def listar_peliculas_route():
    return await listar_peliculas()

@router.get("/peliculas/{id}", response_model=Pelicula)
async def obtener_pelicula_route(id: int):
    return await obtener_pelicula(id)
