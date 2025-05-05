from fastapi import APIRouter
from schemas.usuarios import LoginRequest, RegisterRequest, UsuarioResponse
from services import usuarios_service

router = APIRouter()

@router.post("/login", response_model=UsuarioResponse)
async def login(login_data: LoginRequest):
    return await usuarios_service.login(login_data)

@router.post("/registrar", response_model=UsuarioResponse)
async def registrar(register_data: RegisterRequest):
    return await usuarios_service.registrar(register_data)
