# app/views/cli_view.py

class CLIView:
    def mostrar_bienvenida(self):
        print("\n=== PROYECTO DEPARTAMENTOS Y MUNICIPIOS DE COLOMBIA ===")

    def mostrar_datos(self, lista_datos):
        for item in lista_datos:
            print(f"{item.get('departamento')} - {item.get('municipio')}")
