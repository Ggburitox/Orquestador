from fastapi import APIRouter, Request
from services import usuarios_service

router = APIRouter()

@router.post("/login")
def login(request: Request):
    return usuarios_service.login(request)

@router.post("/registrar")
def registrar(request: Request):
    return usuarios_service.registrar(request)