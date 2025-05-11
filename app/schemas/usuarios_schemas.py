from pydantic import BaseModel, EmailStr, Field

class UsuarioCreate(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=6)
    dni: str = Field(..., min_length=8, max_length=8)

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str

class UsuarioUpdate(BaseModel):
    username: str = Field(None, min_length=3)
    email: EmailStr = None
    password: str = Field(None, min_length=6)
    dni: str = Field(None, min_length=8, max_length=8)

class Usuario(BaseModel):
    id: int
    username: str
    email: EmailStr
    dni: str

    class Config:
        from_attributes = True
