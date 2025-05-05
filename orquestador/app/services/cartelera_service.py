import requests

CARTELERA_URL = "http://cartelera:8080"

def obtener_cartelera():
    return requests.get(f"{CARTELERA_URL}/peliculas").json()