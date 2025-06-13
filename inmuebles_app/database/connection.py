import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # usa tu contraseña de MySQL si tienes una
            database="inmuebles_barranquilla"
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos.")
            return connection
    except Error as e:
        print("Error al conectar a la base de datos:", e)
        return None
