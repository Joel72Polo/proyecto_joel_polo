# tests/test_models.py
import sys
import os
# Añade la raíz del proyecto al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controlador.datos_controller import DatosController
from unittest.mock import Mock, patch

def test_crear_dato():
    mock_insertar = Mock(return_value=None)
    with patch('database.datos_dao.DatosDAO.insertar', new=mock_insertar):
        controlador = DatosController()
        registro_scuep = "573-01"
        anio = 2008
        proyecto = "PoloAS"
        direccion = "Cr22 D"
        unidades = 20
        enajenador = "Pol"
        controlador.crear_dato(registro_scuep, anio, proyecto, direccion, unidades, enajenador)
        expected_data = {
            "registro_scuep": registro_scuep,
            "anio": anio,
            "proyecto": proyecto,
            "direccion": direccion,
            "unidades": unidades,
            "enajenador": enajenador
        }
        mock_insertar.assert_called_once_with(expected_data)