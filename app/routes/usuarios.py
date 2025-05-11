from fastapi import APIRouter
from app.services.usuarios_service import registrar_usuario, login_usuario, obtener_usuario, actualizar_usuario, eliminar_usuario
from app.schemas.usuarios_schemas import UsuarioCreate, UsuarioLogin, UsuarioUpdate, Usuario

router = APIRouter(tags=["Usuarios"])

@router.post("/register", response_model=Usuario)
async def registrar_usuario_route(usuario: UsuarioCreate):
    return await registrar_usuario(usuario)

@router.post("/login")
async def login_usuario_route(login: UsuarioLogin):
    return await login_usuario(login)

@router.get("/{userId}", response_model=Usuario)
async def obtener_usuario_route(userId: int):
    return await obtener_usuario(userId)

@router.put("/{userId}", response_model=Usuario)
async def actualizar_usuario_route(userId: int, usuario: UsuarioUpdate):
    return await actualizar_usuario(userId, usuario)

@router.delete("/{userId}")
async def eliminar_usuario_route(userId: int):
    return await eliminar_usuario(userId)
