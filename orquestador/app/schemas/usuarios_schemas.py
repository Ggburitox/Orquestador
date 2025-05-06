from pydantic import BaseModel, EmailStr, Field

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

class RegisterSchema(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=6)
    dni: str = Field(..., min_length=8, max_length=8)

class UpdateSchema(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr