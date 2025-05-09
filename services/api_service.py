import requests

class APIClient:
    def __init__(self):
        self.url = "https://www.datos.gov.co/resource/95jt-2v3q.json"

    def obtener_datos(self, limit=100, filtro=None):
        params = {"$limit": limit}
        if filtro:
            params.update(filtro)

        try:
            response = requests.get(self.url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error al conectar con la API: {e}")
            return None
