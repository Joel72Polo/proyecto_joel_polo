class CLIView:
    def mostrar_bienvenida(self):
        print("\n=== PROYECTO DEPARTAMENTOS Y MUNICIPIOS DE COLOMBIA ===")

    def mostrar_datos(self, lista_datos):
        if lista_datos:
            for item in lista_datos:
                print(f"{item.get('departamento', 'N/A')} - {item.get('municipio', 'N/A')}")
        else:
            print("No se encontraron datos para mostrar.")
