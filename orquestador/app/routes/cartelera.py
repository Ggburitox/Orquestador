from fastapi import APIRouter
from services import cartelera_service

router = APIRouter()

@router.get("/cartelera")
def obtener_cartelera():
    return cartelera_service.obtener_cartelera()