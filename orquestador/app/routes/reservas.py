from fastapi import APIRouter
from schemas.reservas import ReservaRequest, ReservaResponse
from services import reservas_service
from typing import List

router = APIRouter()

@router.post("/reservar", response_model=ReservaResponse)
async def reservar(reserva_data: ReservaRequest):
    return await reservas_service.reservar(reserva_data)

@router.get("/reservas/{user_id}", response_model=List[ReservaResponse])
def obtener_reservas(user_id: int):
    return reservas_service.obtener_reservas(user_id)
