import httpx

USUARIOS_SERVICE_URL = "http://servicio-usuarios:8001"

async def registrar_usuario(usuario):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{USUARIOS_SERVICE_URL}/servicio-usuarios",
            json=usuario.dict()
        )
        return response.json()

async def login(credenciales):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{USUARIOS_SERVICE_URL}/login",
            json=credenciales.dict()
        )
        return response.json()