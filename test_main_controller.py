import unittest
from unittest.mock import patch
from main_controller import MainController

class TestMainController(unittest.TestCase):

    @patch('services.api_service.APIClient.obtener_datos')
    @patch('app.views.cli_view.CLIView.mostrar_datos')
    @patch('app.views.cli_view.CLIView.mostrar_bienvenida')
    def test_ejecutar(self, mock_bienvenida, mock_mostrar_datos, mock_obtener_datos):
        mock_obtener_datos.return_value = [
            {'departamento': 'Antioquia', 'municipio': 'Medellín'},
            {'departamento': 'Cundinamarca', 'municipio': 'Bogotá'}
        ]

        controller = MainController()
        controller.ejecutar()

        mock_bienvenida.assert_called_once()
        mock_mostrar_datos.assert_called_once_with(mock_obtener_datos.return_value)

if __name__ == '__main__':
    unittest.main()
