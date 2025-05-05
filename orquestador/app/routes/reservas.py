from fastapi import APIRouter, Request
from services import reservas_service

router = APIRouter()

@router.post("/reservar")
def reservar(request: Request):
    return reservas_service.reservar(request)

@router.get("/reservas/{user_id}")
def obtener_reservas(user_id: int):
    return reservas_service.obtener_reservas(user_id)
