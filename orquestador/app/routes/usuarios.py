from fastapi import APIRouter, Depends, HTTPException, status
from typing import Dict, Any

from ..schemas.usuarios_schemas import LoginSchema, RegisterSchema, UpdateSchema
from ..services.usuarios_service import (
    login as service_login,
    registrar as service_registrar,
    obtener_usuario,
    obtener_usuario_actual,
    actualizar_usuario,
    eliminar_usuario,
    logout,
    session
)

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.post("/login")
async def login_route(login_data: LoginSchema) -> Dict[str, Any]:
    """Endpoint para iniciar sesión"""
    result = await service_login(login_data)
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=result["error"]
        )
    return result

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_route(register_data: RegisterSchema) -> Dict[str, Any]:
    """Endpoint para registrar un nuevo usuario"""
    result = await service_registrar(register_data)
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result["error"]
        )
    return result

@router.get("/me")
async def get_current_user() -> Dict[str, Any]:
    """Endpoint para obtener el usuario actual"""
    result = await obtener_usuario_actual()
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=result["error"]
        )
    return result

@router.get("/{user_id}")
async def get_user(user_id: int) -> Dict[str, Any]:
    """Endpoint para obtener un usuario por ID"""
    result = await obtener_usuario(user_id)
    if not result or "error" in result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return result

@router.put("/{user_id}")
async def update_user(user_id: int, datos: UpdateSchema) -> Dict[str, Any]:
    """Endpoint para actualizar un usuario"""
    result = await actualizar_usuario(user_id, datos)
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result["error"]
        )
    return result

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int) -> Dict[str, Any]:
    """Endpoint para eliminar un usuario"""
    result = await eliminar_usuario(user_id)
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result["error"]
        )
    return result

@router.post("/logout")
async def logout_route() -> Dict[str, str]:
    """Endpoint para cerrar sesión"""
    return await logout()