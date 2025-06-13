from controlador.datos_controller import DatosController
import mysql.connector

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
        print("6. Salir")
        print("7. Ver últimos registros directamente desde la base de datos")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            controlador.cargar_datos_publicos()

        elif opcion == "2":
            try:
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
            for registro in registros:
                print(registro)

        elif opcion == "4":
            try:
                id_registro = int(input("Ingrese el ID del registro a actualizar: "))
                nuevo_proyecto = input("Ingrese el nuevo nombre del proyecto: ")
                controlador.actualizar_dato(id_registro, nuevo_proyecto)
                print("Registro actualizado correctamente.")
            except ValueError:
                print("Error: ID debe ser un valor numérico.")

        elif opcion == "5":
            try:
                id_registro = int(input("Ingrese el ID del registro a eliminar: "))
                controlador.eliminar_dato(id_registro)
                print("Registro eliminado correctamente.")
            except ValueError:
                print("Error: ID debe ser un valor numérico.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        elif opcion == "7":
            print("\nÚltimos registros desde la base de datos:")
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="inmuebles_barranquilla"
                )
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM registros_inmuebles ORDER BY id DESC LIMIT 5")
                registros = cursor.fetchall()
                for r in registros:
                    print(r)
                cursor.close()
                conn.close()
            except Exception as e:
                print("Error al conectar o consultar la base de datos:", e)

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
