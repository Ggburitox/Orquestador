from fastapi import APIRouter
from typing import List
from app.services.reservas_service import crear_reserva, listar_reservas, reservas_por_usuario, reservas_por_pelicula, eliminar_reserva
from app.schemas.reservas_schemas import Reserva, ReservaCreate

router = APIRouter(tags=["Reservas"])

@router.get("/all", response_model=List[Reserva])
async def listar_reservas_route():
    return await listar_reservas()

@router.get("/usuario/{id}", response_model=List[Reserva])
async def reservas_usuario_route(id: int):
    return await reservas_por_usuario(id)

@router.get("/pelicula/{id}", response_model=List[Reserva])
async def reservas_pelicula_route(id: int):
    return await reservas_por_pelicula(id)

@router.post("/", response_model=Reserva)
async def crear_reserva_route(reserva: ReservaCreate):
    return await crear_reserva(reserva)

@router.delete("/reserva/{id}")
async def eliminar_reserva_route(id: str):
    return await eliminar_reserva(id)
