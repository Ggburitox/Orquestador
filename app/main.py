from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import cartelera, usuarios, reservas

app = FastAPI(
    title="API de Microservicios",
    description="API para gestionar usuarios, cartelera y reservas",
    version="1.0.0"
)

# Este orquestador consume servicios externos:
# - Servicio de películas (FastAPI): http://localhost:8001
# - Servicio de reservas (Spring Boot): http://localhost:8080
# - Servicio de usuarios (Express.js): http://localhost:3000

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajustar en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cartelera.router, prefix="/cartelera")
app.include_router(usuarios.router, prefix="/usuarios")
app.include_router(reservas.router, prefix="/reservas")

@app.get("/")
async def root():
    return {"message": "API de microservicios"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
