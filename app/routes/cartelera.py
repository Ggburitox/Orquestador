from fastapi import APIRouter
from services import cartelera_service
from schemas.cartelera import PeliculaResponse
from typing import List

router = APIRouter()

@router.get("/cartelera", response_model=List[PeliculaResponse])
def obtener_cartelera():
    return cartelera_service.obtener_cartelera()