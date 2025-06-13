from controlador.datos_controller import DatosController
import mysql.connector

# Configuración de la base de datos
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "inmuebles_barranquilla"
}

# Función para conectar con la base de datos
def conectar_db():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print("Error al conectar con la base de datos:", e)
        return None

# Mostrar últimos registros desde la base de datos
def mostrar_ultimos_registros():
    print("\nÚltimos registros desde la base de datos:")
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM registros_inmuebles ORDER BY id DESC LIMIT 5")
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
        except Exception as e:
            print("Error al consultar la base de datos:", e)
        finally:
            cursor.close()
            conn.close()

# Vista (interfaz con el usuario)
def mostrar_menu():
    controlador = DatosController()

    while True:
        print("\n--- Menú de Operaciones ---")
        print("1. Cargar datos públicos en la base de datos")
        print("2. Crear un nuevo registro")
        print("3. Mostrar todos los registros")
        print("4. Actualizar un registro")
        print("5. Eliminar un registro")
        print("6. Ver últimos registros directamente desde la base de datos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            controlador.cargar_datos_publicos()
            print("Datos públicos cargados correctamente.")

        elif opcion == "2":
            try:
                print("\n--- Crear un nuevo registro ---")
                registro_scuep = input("Ingrese el registro SCUEP: ")
                anio = int(input("Ingrese el año: "))
                proyecto = input("Ingrese el nombre del proyecto: ")
                direccion = input("Ingrese la dirección: ")
                unidades = int(input("Ingrese el número de unidades: "))
                enajenador = input("Ingrese el enajenador: ")

                controlador.crear_dato(registro_scuep, anio, proyecto, direccion, unidades, enajenador)
                print("Registro creado correctamente.")
            except ValueError:
                print("Error: Año y unidades deben ser valores numéricos.")

        elif opcion == "3":
            registros = controlador.listar_datos()
            print("\n--- Todos los registros ---")
            for registro in registros:
                print(registro)

        elif opcion == "4":
            try:
                print("\n--- Actualizar un registro ---")
                id_registro = int(input("Ingrese el ID del registro a actualizar: "))
                nuevo_proyecto = input("Ingrese el nuevo nombre del proyecto: ")
                controlador.actualizar_dato(id_registro, nuevo_proyecto)
                print("Registro actualizado correctamente.")
            except ValueError:
                print("Error: ID debe ser un valor numérico.")

        elif opcion == "5":
            try:
                print("\n--- Eliminar un registro ---")
                id_registro = int(input("Ingrese el ID del registro a eliminar: "))
                controlador.eliminar_dato(id_registro)
                print("Registro eliminado correctamente.")
            except ValueError:
                print("Error: ID debe ser un valor numérico.")

        elif opcion == "6":
            mostrar_ultimos_registros()

        elif opcion == "7":
            print("Saliendo del programa... ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
