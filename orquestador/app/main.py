from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import cartelera, usuarios, reservas
app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



app = FastAPI()
app.include_router(cartelera.router)
app.include_router(usuarios.router)
app.include_router(reservas.router)
@app.get("/health")
async def health_check():
    return {"status": "ok"}