from database.connection import get_connection

conn = get_connection()
if conn:
    print("La conexión fue exitosa.")
    conn.close()
else:
    print("Fallo la conexión.")
