from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import cartelera, usuarios, reservas

app = FastAPI(
    title="API de Microservicios",
    description="API para gestionar usuarios, cartelera y reservas",
    version="1.0.0"
)
# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajustar en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(cartelera.router)
app.include_router(usuarios.router)
app.include_router(reservas.router)
@app.get("/")
async def root():
    return {"message": "API de microservicios"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)