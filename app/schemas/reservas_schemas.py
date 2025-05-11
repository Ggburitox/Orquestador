from pydantic import BaseModel
from typing import Optional
from datetime import date

class ReservaBase(BaseModel):
    usuario: Optional[str]
    fecha: date
    pelicula_nombre: str
    peliculaId: int
    usuarioId: int

class ReservaCreate(ReservaBase):
    pass

class Reserva(ReservaBase):
    id: str

    class Config:
        from_attributes = True
