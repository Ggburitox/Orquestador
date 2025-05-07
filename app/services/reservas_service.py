import requests

RESERVAS_URL = "http://reservas:3001"

async def reservar(reserva_data):
    response = requests.post(f"{RESERVAS_URL}/reservas", json=reserva_data.dict())
    return response.json()

def obtener_reservas(user_id):
    return requests.get(f"{RESERVAS_URL}/reservas/usuario/{user_id}").json()
