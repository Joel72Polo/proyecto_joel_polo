# app/controllers/main_controller.py

from app.models.data_model import DataModel
from app.views.cli_view import CLIView

class MainController:
    def __init__(self):
        self.modelo = DataModel()
        self.vista = CLIView()

    def iniciar(self):
        self.vista.mostrar_bienvenida()
        datos = self.modelo.obtener_departamentos_municipios(limite=10)
        self.vista.mostrar_datos(datos)
