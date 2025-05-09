from services.api_service import APIClient
from app.views.cli_view import CLIView

class MainController:
    def __init__(self):
        self.api_client = APIClient()
        self.view = CLIView()

    def ejecutar(self):
        self.view.mostrar_bienvenida()
        datos = self.api_client.obtener_datos(limit=10)  # Límite de 10 por defecto
        self.view.mostrar_datos(datos)

if __name__ == "__main__":
    controller = MainController()
    controller.ejecutar()

