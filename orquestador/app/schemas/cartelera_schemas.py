from pydantic import BaseModel

class PeliculaResponse(BaseModel):
    id: int
    titulo: str
    descripcion: str
    duracion: int
