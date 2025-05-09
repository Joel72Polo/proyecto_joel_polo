from app.views.cli_view import CLIView
from app.models.data_model import DataModel

class MainController:
    def __init__(self):
        self.vista = CLIView()
        self.modelo = DataModel()

    def iniciar(self):
        self.vista.mostrar_bienvenida()
        # Aquí se conectará con la API y mostrará opciones CRUD
