import requests
USUARIOS_URL = "http://usuarios:3000"

def login(request):
    return requests.post(f"{USUARIOS_URL}/login", json=request.json()).json()

def registrar(request):
    return requests.post(f"{USUARIOS_URL}/registrar", json=request.json()).json()