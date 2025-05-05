import requests
RESERVAS_URL = "http://reservas:3001"

def reservar(request):
    return requests.post(f"{RESERVAS_URL}/reservas", json=request.json()).json()

def obtener_reservas(user_id):
    return requests.get(f"{RESERVAS_URL}/reservas/usuario/{user_id}").json()