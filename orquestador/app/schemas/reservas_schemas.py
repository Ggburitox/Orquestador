from pydantic import BaseModel

class ReservaRequest(BaseModel):
    user_id: int
    funcion_id: int
    cantidad_boletos: int

class ReservaResponse(BaseModel):
    id: int
    user_id: int
    funcion_id: int
    cantidad_boletos: int
    estado: str
