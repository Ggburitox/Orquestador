from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services import usuarios_service, cartelera_service, reservas_service
from schemas import UsuarioCreate, LoginRequest, ReservaCreate

app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/registrar")
async def registrar_usuario(usuario: UsuarioCreate):
    return await usuarios_service.registrar_usuario(usuario)

@app.post("/login")
async def login(credenciales: LoginRequest):
    return await usuarios_service.login(credenciales)

@app.get("/peliculas")
async def obtener_peliculas():
    return await cartelera_service.obtener_peliculas()

@app.post("/reservar")
async def crear_reserva(reserva: ReservaCreate):
    return await reservas_service.crear_reserva(reserva)

@app.get("/health")
async def health_check():
    return {"status": "ok"}