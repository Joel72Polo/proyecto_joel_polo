# Sistema de Gestión de Datos Abiertos de Colombia - Entrega 3

## Objetivo
Desarrollar una app web con Flask para gestionar registros de inmuebles en Barranquilla desde datos.gov.co, con CRUD, búsqueda/filtrado y validación robusta.

## Estructura del Dataset
Fuente: https://www.datos.gov.co/Vivienda-Ciudad-y-Territorio/Registro-de-venta-de-inmuebles-en-enajenador-de-Ba/2b8b-8hn5/about_data.

| Campo         | Tipo      | Descripción           | Ejemplo      |
|---------------|-----------|-----------------------|--------------|
| registro_scuep| VARCHAR(255) | ID único             | 0157-04      |
| anio          | INT        | Año                   | 2004         |
| proyecto      | VARCHAR(255) | Nombre proyecto      | EDIFICIO MALIBU |
| direccion     | VARCHAR(255) | Dirección            | C 80 51 40   |
| unidades      | INT        | Unidades              | 20           |
| enajenador    | VARCHAR(255) | Vendedor             | CONSTRUCCIONES CARES |

**Notas:** `unidades` y `anio` se validan y convierten a enteros, asignando 0 si falla (rango `anio`: 1900-2025).

## Implementación
- **Modelo (DAO):** `DatosDAO` para CRUD; `DatosController` para lógica y validación.
- **Métodos:** `crear_dato()`, `listar_datos()`, `actualizar_dato()`, `eliminar_dato()`, `buscar_datos()`.

## Ejecución
1. **Requisitos:** Python 3.x, Lanza la aplicación CLI o Flask según prefieras, mysql-connector-python, XAMPP, VS Code.
2. **Configuración MySQL (XAMPP):**
   - Inicia Apache y MySQL en XAMPP.
   - Crea la DB `inmuebles_barranquilla` en phpMyAdmin e importa `inmuebles_barranquilla.sql`.
   - Ajusta `connection.py`: `host="localhost"`, `user="root"`, `password=""`, `database="inmuebles_barranquilla"`.
3. **Lanzar:** `python vista_flask.py`, accede a `http://127.0.0.1:5000/`. # Para la aplicación Flask
`python vista_cli.py` # Para la interfaz CLI

## Para pruebas**: Ejecuta las pruebas unitarias con:
- `python -m pytest tests/`

## Potencial Comercial
Plataforma de inteligencia inmobiliaria con análisis de mercado, reportes interactivos, predicciones y oportunidades para agencias, constructoras, inversores, bancos y evaluadores.

**Contribución:** Extrae, procesa y muestra datos vía web mejorada.

**Notas:** Se recomienda usar un entorno virtual en Windows: `python -m venv venv` y activarlo con `venv\Scripts\activate`.
- Asegúrate de que las carpetas `controlador` y `database` contengan archivos `__init__.py` válidos.
- Si hay errores de importación, ajusta `sys.path` en `test_models.py`.

## Mejoras Futuras
- Visualizaciones (gráficos/mapas).
- Autenticación y roles.
- Exportación a CSV/PDF.

## Cumplimiento de Requisitos
Cumple con Entrega 3:
- Interfaz web optimizada con CRUD, búsqueda/filtrado.
- Validación robusta de datos (campos obligatorios, rangos).
- Mejor experiencia de usuario con retroalimentación.



## Autor
* Joel Polo Caicedo