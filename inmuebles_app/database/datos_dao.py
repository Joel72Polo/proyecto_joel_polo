from database.connection import get_connection

class DatosDAO:

    @staticmethod
    def obtener_todos():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM registros_inmuebles")
        resultados = cursor.fetchall()
        cursor.close()
        connection.close()
        return resultados

    @staticmethod
    def insertar(datos):
        connection = get_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO registros_inmuebles
            (registro_scuep, anio, proyecto, direccion, unidades, enajenador)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            datos["registro_scuep"],
            datos["anio"],
            datos["proyecto"],
            datos["direccion"],
            datos["unidades"],
            datos["enajenador"]
        ))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def actualizar(id_registro, nuevo_proyecto):
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE registros_inmuebles SET proyecto = %s WHERE id = %s"
        cursor.execute(query, (nuevo_proyecto, id_registro))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def eliminar(id_registro):
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM registros_inmuebles WHERE id = %s"
        cursor.execute(query, (id_registro,))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def cargar_publicos(filas):
        connection = get_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO registros_inmuebles
            (registro_scuep, anio, proyecto, direccion, unidades, enajenador)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.executemany(query, filas)
        connection.commit()
        cursor.close()
        connection.close()

