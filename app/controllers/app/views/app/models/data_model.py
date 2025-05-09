import requests

class DataModel:
    def obtener_datos(self):
        # Aquí puedes usar la API pública
        url = "https://www.datos.gov.co/resource/XXXX.json"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            return []
