import httpx
from app.schemas.cartelera_schemas import PeliculaCreate

CARTELERA_URL = "http://54.166.101.85:8002/peliculas"

async def crear_pelicula(pelicula: PeliculaCreate):
    async with httpx.AsyncClient() as client:
        response = await client.post(CARTELERA_URL, json=pelicula.dict())
        response.raise_for_status()
        return response.json()

async def listar_peliculas():
    async with httpx.AsyncClient() as client:
        response = await client.get(CARTELERA_URL)
        response.raise_for_status()
        return response.json()

async def obtener_pelicula(id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{CARTELERA_URL}/{id}")
        response.raise_for_status()
        return response.json()
