# app/models/data_model.py

import requests

class DataModel:
    def obtener_departamentos_municipios(self, limite=100):
        url = "https://www.datos.gov.co/resource/xdk5-pm3f.json"
        params = {"$limit": limite}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la API: {e}")
            return []
