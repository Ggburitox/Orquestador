import httpx
from app.schemas.reservas_schemas import ReservaCreate

RESERVAS_URL = "http://54.166.101.85:8081/reservas"

async def listar_reservas():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{RESERVAS_URL}/all")
        response.raise_for_status()
        return response.json()

async def reservas_por_usuario(id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{RESERVAS_URL}/usuario/{id}")
        response.raise_for_status()
        return response.json()

async def reservas_por_pelicula(id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{RESERVAS_URL}/pelicula/{id}")
        response.raise_for_status()
        return response.json()

async def crear_reserva(reserva: ReservaCreate):
    async with httpx.AsyncClient() as client:
        response = await client.post(RESERVAS_URL, json=reserva.dict())
        response.raise_for_status()
        return response.json()

async def eliminar_reserva(id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{RESERVAS_URL}/reserva/{id}")
        response.raise_for_status()
        return {"message": "Reserva eliminada"}
