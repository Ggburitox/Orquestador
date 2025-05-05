import requests

USUARIOS_URL = "http://usuarios:3000"

async def login(login_data):
    response = requests.post(f"{USUARIOS_URL}/login", json=login_data.dict())
    return response.json()

async def registrar(register_data):
    response = requests.post(f"{USUARIOS_URL}/registrar", json=register_data.dict())
    return response.json()