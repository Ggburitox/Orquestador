import httpx
from app.schemas.usuarios_schemas import UsuarioCreate, UsuarioLogin, UsuarioUpdate

USUARIOS_URL = "http://54.166.101.85:8001/usuarios"

async def registrar_usuario(usuario: UsuarioCreate):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USUARIOS_URL}/register", json=usuario.dict())
        response.raise_for_status()
        return response.json()

async def login_usuario(login: UsuarioLogin):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USUARIOS_URL}/login", json=login.dict())
        response.raise_for_status()
        return response.json()

async def obtener_usuario(userId: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USUARIOS_URL}/{userId}")
        response.raise_for_status()
        return response.json()

async def actualizar_usuario(userId: int, usuario: UsuarioUpdate):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{USUARIOS_URL}/{userId}", json=usuario.dict(exclude_unset=True))
        response.raise_for_status()
        return response.json()

async def eliminar_usuario(userId: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{USUARIOS_URL}/{userId}")
        response.raise_for_status()
        return {"message": "Usuario eliminado"}
