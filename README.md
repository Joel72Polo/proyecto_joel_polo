Sistema de Gestión de Datos Abiertos de Colombia - Entrega 3
Objetivo
Desarrollar una aplicación web con Flask para gestionar registros de inmuebles en Barranquilla desde datos.gov.co, con CRUD, búsqueda/filtrado y validación robusta.

Estructura del conjunto de datos
Fuente: https://www.datos.gov.co/Vivienda-Ciudad-y-Territorio/Registro-de-venta-de-inmuebles-en-enajenador-de-Ba/2b8b-8hn5/about_data .

Campo	Tipo	Descripción	Ejemplo
registro_scuep	VARCHAR(255)	Identificación única	0157-04
anio	INT	Año	2004
proyecto	VARCHAR(255)	Nombre del proyecto	EDIFICIO MALIBU
dirección	VARCHAR(255)	Dirección	C 80 51 40
unidades	INT	Unidades	20
enajenador	VARCHAR(255)	Vendedor	CONSTRUCCIONES CARES
Notas: unidades y aniose validan y convierten a enteros, asignando 0 si falla (rango anio: 1900-2025).

Implementación
Modelo (DAO): DatosDAO para CRUD; DatosControllerpara lógica y validación.
Métodos: crear_dato() , listar_datos(), actualizar_dato(), eliminar_dato(), buscar_datos().
Ejecución
Requisitos: Python 3.x, Lanzar la aplicación CLI o Flask según preferencias, mysql-connector-python, XAMPP, VS Code.
Configuración MySQL (XAMPP):
Inicia Apache y MySQL en XAMPP.
Crea la base de datos inmuebles_barranquillaen phpMyAdmin e importa inmuebles_barranquilla.sql.
Ajusta connection.py: host="localhost", user="root", password="", database="inmuebles_barranquilla".
Lanzar: python vista_flask.py , acceder a http://127.0.0.1:5000/. # Para la aplicación Flask python vista_cli.py# Para la interfaz CLI
Para pruebas**: Ejecuta las pruebas unitarias con:
python -m pytest tests/
Potencial Comercial
Plataforma de inteligencia inmobiliaria con análisis de mercado, informes interactivos, predicciones y oportunidades para agencias, constructoras, inversores, bancos y evaluadores.

Contribución: Extrae, procesa y muestra datos vía web mejorada.

Notas: Se recomienda usar un entorno virtual en Windows: python -m venv venvy activarlo con venv\Scripts\activate.

Asegúrese de que las carpetas controladory databasecontengan archivos __init__.pyválidos.
Si hay errores de importación, ajusta sys.pathen test_models.py.
Mejoras futuras
Visualizaciones (gráficos/mapas).
Autenticación y roles.
Exportación a CSV/PDF.
Cumplimiento de requisitos
Cumpleaños con Entrega 3:

Interfaz web optimizada con CRUD, búsqueda/filtrado.
Validación robusta de datos (campos obligatorios, rangos).
Mejor experiencia de usuario con retroalimentación.
Autor
Joel Polo Caicedo
