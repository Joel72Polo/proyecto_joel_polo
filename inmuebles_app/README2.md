# Sistema de Gestión de Datos Abiertos de Colombia - Entrega 2

## Objetivo del Proyecto

Este proyecto desarrolla una aplicación en Python para consumir datos de la API de datos.gov.co, almacenarlos en una base de datos relacional (MySQL), y permitir operaciones CRUD (Crear, Leer, Actualizar, Eliminar) a través de una interfaz de línea de comandos (CLI).  Esta entrega (Entrega 2) se centra en la implementación del Modelo (DAO) y las operaciones CRUD básicas.

## Estructura del Dataset

El dataset utilizado proviene de https://www.datos.gov.co/Vivienda-Ciudad-y-Territorio/Registro-de-venta-de-inmuebles-en-enajenador-de-Ba/2b8b-8hn5/about_data.  Contiene información sobre registros de venta de inmuebles en Barranquilla.

La estructura del dataset es la siguiente:

| Campo             | Tipo de Dato | Descripción                                  | Ejemplo          |
|-------------------|--------------|----------------------------------------------|------------------|
| registro_scuep    | VARCHAR(50)  | Identificador único del registro            | 0157-04          |
| anio              | INT          | Año del registro                             | 2004             |
| proyecto          | VARCHAR(255) | Nombre del proyecto inmobiliario             | EDIFICIO MALIBU  |
| direccion         | VARCHAR(255) | Dirección del inmueble                       | C 80 51 40       |
| unidades          | INT          | Número de unidades en el proyecto            | 20               |
| enajenador        | VARCHAR(255) | Nombre del enajenador (vendedor)             | CONSTRUCCIONES CARES |

**Notas Importantes sobre el Dataset:**

* La columna `unidades` puede contener valores no numéricos como "LOTES", "9 LOTES", "8LOTES", "ADI- 2", "70-12 LC" y "77+9". El programa intenta convertir estos valores a enteros, extrayendo el número si es posible, o asignando 0 si no se puede convertir.
* La columna `anio` puede contener comas (por ejemplo, "2,004"). El programa elimina las comas antes de convertir el valor a entero.

## Implementación del Modelo (DAO)

El Modelo se implementa utilizando un Data Access Object (DAO) para interactuar con la base de datos MySQL. El DAO encapsula la lógica de acceso a datos y proporciona métodos para realizar las operaciones CRUD.

Las principales clases del Modelo son:

* `RegistroInmueble`: Representa una entidad de registro de inmueble en la base de datos.
* `RegistroInmuebleDAO`: Proporciona los métodos para interactuar con la tabla `registros_inmuebles`.

Los métodos CRUD implementados son:

* `crear_registro(registro)`: Crea un nuevo registro en la base de datos.
* `leer_registros()`: Obtiene todos los registros de la base de datos.
* `actualizar_registro(id, registro)`: Actualiza un registro existente.
* `eliminar_registro(id)`: Elimina un registro de la base de datos.

## Cómo Ejecutar el Programa

1.  **Requisitos Previos:**
    * Python 3.x instalado.
    * La biblioteca `requests` instalada (`pip install requests`).
    * La biblioteca `csv` (generalmente incluida con Python).
    * El conector de MySQL para Python (`mysql-connector-python` - `pip install mysql-connector-python`). **NOTA IMPORTANTE: Asegúrate de que MySQL está funcionando correctamente en XAMPP.**
    * XAMPP instalado y configurado.
    * Visual Studio Code (VS Code) instalado (recomendado para desarrollo).

2.  **Configuración de la Base de Datos (MySQL con XAMPP):**
    * **Iniciar XAMPP:**
        * Abre el panel de control de XAMPP.
        * Inicia los servicios de **Apache** y **MySQL**.
    * **Crear la Base de Datos:**
        * Abre tu navegador web y navega a `http://localhost/phpmyadmin`. (phpMyAdmin es una herramienta para administrar MySQL).
        * En phpMyAdmin, haz clic en "Bases de datos".
        * Ingresa el nombre de la base de datos (`inmuebles_barranquilla`) y haz clic en "Crear".
        * **Importar el Esquema:**
            * En phpMyAdmin, selecciona la base de datos que acabas de crear.
            * Haz clic en la pestaña "Importar".
            * Haz clic en "Seleccionar archivo" y elige el archivo SQL (`inmuebles_barranquilla.sql`).
            * Haz clic en "Continuar" para ejecutar el script SQL y crear la tabla `registros_inmuebles`.
    * **Ajustar Detalles de Conexión en `database/connection.py`:**
        * Abre el archivo `database/connection.py` en tu editor de código.
        * Modifica las variables de conexión para que coincidan con tu configuración de XAMPP. Normalmente, la configuración predeterminada de XAMPP es: `connection.py`
            ```python
            host = "localhost"
            user = "root"
            password = ""  # La contraseña suele estar vacía por defecto
            database = "inmuebles_barranquilla"  # El nombre de la base de datos
            ```
        * Asegúrate de que el `host`, `user`, `password`, y `database` sean correctos.

3.  **Ejecución del Programa:**
    * **Usando la terminal de VS Code (Recomendado):**
        * Abre el proyecto en VS Code.
        * Abre la terminal integrada de VS Code (Ver -> Terminal o Ctrl+`).
        * Navega al directorio del proyecto (si no estás ya en él) usando el comando `cd`.
        * Ejecuta el script principal: `python app_registros_inmuebles.py`
    * **Usando la terminal del sistema:**
        * Abre tu terminal o línea de comandos (cmd en Windows, Terminal en macOS/Linux).
        * Navega al directorio del proyecto usando el comando `cd`.
        * Ejecuta el script principal: `python app_registros_inmuebles.py`

4.  **Uso:**
    * El programa mostrará un menú de opciones.
    * Selecciona la opción deseada (por ejemplo, "1" para cargar datos públicos).
    * Sigue las instrucciones en pantalla.

## Manejo de Errores

El programa incluye mecanismos para manejar los siguientes errores:

* **`ValueError` al convertir datos:** Se captura la excepción `ValueError` al intentar convertir cadenas a enteros (por ejemplo, al leer los datos del CSV o al recibir entrada del usuario). Se imprimen mensajes de advertencia y se toman medidas para continuar la ejecución (por ejemplo, saltar la fila o usar un valor predeterminado).

## Potencial Comercial: Plataforma de Inteligencia de Mercado Inmobiliario

Este software tiene un fuerte potencial para desarrollar una plataforma de inteligencia de mercado inmobiliario. Al extraer y analizar datos de fuentes públicas (como datos.gov.co) y combinarlo con datos adicionales, se puede ofrecer información valiosa a diversos actores del sector.

**Propuesta de Valor:**

* **Análisis Detallado del Mercado:** Proporcionar análisis en profundidad de tendencias de precios, oferta y demanda, tiempo de venta, y otros indicadores clave por zona geográfica, tipo de propiedad, y rango de precios.
* **Reportes Automatizados e Interactivos:** Generar reportes periódicos sobre el estado del mercado, así como dashboards interactivos que permitan a los usuarios explorar los datos y personalizar sus consultas.
* **Predicciones y Pronósticos:** Utilizar técnicas de análisis predictivo para estimar la futura evolución de los precios y la demanda, ayudando a los usuarios a tomar decisiones de inversión más informadas.
* **Identificación de Oportunidades:** Detectar zonas con potencial de valorización, nichos de mercado desatendidos, y otros factores que influyen en el éxito de las transacciones inmobiliarias.

**Clientes Potenciales:**

* **Agencias Inmobiliarias:** Para mejorar la precisión de sus valoraciones, identificar clientes potenciales, y optimizar sus estrategias de marketing.
* **Constructoras:** Para evaluar la viabilidad de nuevos proyectos, seleccionar ubicaciones estratégicas, y ajustar su oferta a la demanda del mercado.
* **Inversionistas:** Para identificar oportunidades de inversión rentables, evaluar el riesgo, y maximizar el retorno de su capital.
* **Bancos y Entidades Financieras:** Para realizar valoraciones de propiedades, evaluar el riesgo crediticio, y ofrecer productos financieros adaptados a las necesidades del mercado.
* **Evaluadores de Propiedades:** Para realizar tasaciones más precisas y objetivas, respaldadas por datos de mercado actualizados.

**Cómo el Software Actual Contribuye:**

El software desarrollado en este proyecto proporciona la base para esta plataforma al:

* **Extraer y Almacenar Datos:** Automatiza la recopilación y el almacenamiento de datos relevantes del sector inmobiliario desde fuentes públicas.
* **Procesar y Limpiar Datos:** Implementa mecanismos para manejar la inconsistencia y los errores en los datos, asegurando su calidad para el análisis.
* **Ofrecer una API (Potencial):** Puede ser ampliado para proporcionar una API que permita a otras aplicaciones y sistemas acceder a los datos procesados.

**Próximos Pasos:**

Para convertir este software en una plataforma comercial, se requerirían las siguientes mejoras:

* **Interfaz Web:** Desarrollar una interfaz web intuitiva y fácil de usar para que los clientes puedan acceder a los datos y las herramientas de análisis.

## Mejoras Futuras

* Implementar una interfaz web en lugar de una CLI.
* Agregar validación de datos más robusta.
* Agregar funcionalidades de búsqueda y filtrado.

## Autor

* Joel Polo Caicedo