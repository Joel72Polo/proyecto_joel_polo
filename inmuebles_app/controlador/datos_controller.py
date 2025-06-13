import csv
import requests
import re
from database.datos_dao import DatosDAO

class DatosController:
    def listar_datos(self):
        return DatosDAO.obtener_todos()

    def crear_dato(self, registro_scuep, anio, proyecto, direccion, unidades, enajenador):
        nuevo_dato = {
            "registro_scuep": registro_scuep,
            "anio": anio,
            "proyecto": proyecto,
            "direccion": direccion,
            "unidades": unidades,
            "enajenador": enajenador
        }
        return DatosDAO.insertar(nuevo_dato)

    def actualizar_dato(self, id_registro, nuevo_proyecto):
        return DatosDAO.actualizar(id_registro, nuevo_proyecto)

    def eliminar_dato(self, id_registro):
        return DatosDAO.eliminar(id_registro)

    def cargar_datos_publicos(self):
        def extraer_numero(texto):
            match = re.search(r'\d+', texto)
            return int(match.group(0)) if match else 0

        url = "https://www.datos.gov.co/api/views/2b8b-8hn5/rows.csv?accessType=DOWNLOAD"
        try:
            print("Descargando datos desde fuente pública...")
            response = requests.get(url)
            response.raise_for_status()
            datos = response.content.decode("utf-8").splitlines()

            reader = csv.reader(datos)
            next(reader)  # Saltar encabezado

            unidades_mapping = {
                "LOTES": 1,
                "9 LOTES": 9,
                "8LOTES": 8,
                "ADI- 2": 2,
                "70-12 LC": 82,
                "77+9": 86
            }

            filas = []
            for fila in reader:
                if len(fila) < 6:
                    continue

                try:
                    anio = int(fila[1].replace(",", ""))
                except ValueError:
                    continue

                unidades_str = fila[4].upper()
                unidades = unidades_mapping.get(unidades_str, extraer_numero(unidades_str))

                filas.append((
                    fila[0],  # registro_scuep
                    anio,
                    fila[2],  # proyecto
                    fila[3],  # direccion
                    unidades,
                    fila[5]   # enajenador
                ))

            DatosDAO.cargar_publicos(filas)
            print("Datos cargados correctamente.")
        except Exception as e:
            print(f"Error al cargar los datos: {e}")


