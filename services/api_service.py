# services/api_service.py
import requests

class APIClient:
    def __init__(self):
        self.url = "https://www.datos.gov.co/resource/95jt-2v3q.json"

    def obtener_datos(self, limit=100):
        params = {"$limit": limit}
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener datos: {response.status_code}")
