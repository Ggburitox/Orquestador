import requests
from typing import Dict, Any
from ..schemas.usuarios_schemas import LoginSchema, RegisterSchema, UpdateSchema

# URL base para el servicio de usuarios
USUARIOS_URL = "http://usuarios:3000"


# Clase para gestionar la sesión del usuario
class UserSession:
    def __init__(self):
        self.user_id = None
        self.token = None
        self.user_data = None

    def set_session(self, user_id, token, user_data):
        self.user_id = user_id
        self.token = token
        self.user_data = user_data

    def clear_session(self):
        self.user_id = None
        self.token = None
        self.user_data = None

    @property
    def is_authenticated(self):
        return self.token is not None

    def get_auth_headers(self):
        if not self.token:
            return {}
        return {"Authorization": f"Bearer {self.token}"}


# Instancia global de sesión
session = UserSession()


async def login(login_data: LoginSchema) -> Dict[str, Any]:
    """Realiza el login y guarda los datos de sesión"""
    response = requests.post(f"{USUARIOS_URL}/login", json=login_data.dict())
    result = response.json()

    if response.status_code == 200 and "user" in result and "token" in result:
        user_id = result["user"]["id"]
        token = result["token"]
        session.set_session(user_id, token, result["user"])
        print(f"Login exitoso. Usuario ID: {user_id}")

    return result


async def registrar(register_data: RegisterSchema) -> Dict[str, Any]:
    """Registra un nuevo usuario"""
    response = requests.post(f"{USUARIOS_URL}/register", json=register_data.dict())
    result = response.json()

    if response.status_code == 201 and "id" in result:
        print(f"Registro exitoso. Usuario ID: {result['id']}")

    return result


async def obtener_usuario(user_id: int) -> Dict[str, Any]:
    """Obtiene los datos de un usuario por su ID"""
    headers = session.get_auth_headers()
    response = requests.get(f"{USUARIOS_URL}/{user_id}", headers=headers)
    return response.json()


async def obtener_usuario_actual() -> Dict[str, Any]:
    """Obtiene los datos del usuario actualmente autenticado"""
    if not session.is_authenticated:
        return {"error": "No hay usuario autenticado"}

    return await obtener_usuario(session.user_id)


async def actualizar_usuario(user_id: int, datos_actualizacion: UpdateSchema) -> Dict[str, Any]:
    """Actualiza los datos de un usuario"""
    headers = session.get_auth_headers()
    response = requests.put(
        f"{USUARIOS_URL}/{user_id}",
        json=datos_actualizacion.dict(),
        headers=headers
    )
    result = response.json()

    if response.status_code == 200 and session.user_id == user_id:
        session.user_data.update(result)

    return result


async def eliminar_usuario(user_id: int) -> Dict[str, Any]:
    """Elimina un usuario por su ID"""
    headers = session.get_auth_headers()
    response = requests.delete(f"{USUARIOS_URL}/{user_id}", headers=headers)

    if response.status_code == 204 and session.user_id == user_id:
        session.clear_session()
        return {"message": "Usuario eliminado correctamente. Sesión cerrada."}

    if response.status_code == 204:
        return {"message": "Usuario eliminado correctamente"}

    return response.json()


async def logout() -> Dict[str, str]:
    """Cierra la sesión del usuario actual"""
    if not session.is_authenticated:
        return {"message": "No hay sesión activa"}

    session.clear_session()
    return {"message": "Sesión cerrada correctamente"}