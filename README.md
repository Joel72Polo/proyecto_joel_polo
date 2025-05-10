# proyecto_joel_polo

Aplicación en Python estructurada con el patrón **MVC (Modelo - Vista - Controlador)** para consumir y gestionar datos abiertos de Colombia desde [datos.gov.co](https://www.datos.gov.co/).

---

## Objetivo

Crear una aplicación en Python que:

- Consuma un conjunto de datos desde una API pública.
- Almacene la información en una base de datos local.
- Permita realizar operaciones CRUD desde una interfaz de línea de comandos (CLI).
- Siga el patrón de diseño **MVC** para mantener el código organizado, escalable y testeable.

---

## Descripción del Proyecto

Este proyecto tiene como propósito gestionar datos del conjunto:

**Departamentos y Municipios de Colombia**  
[Ver dataset en datos.gov.co](https://www.datos.gov.co/Geograf-a-y-Cartograf-a/Departamentos-y-Municipios-de-Colombia/95jt-2v3q)

Se descargan datos geográficos de todos los municipios del país, los cuales contienen:

| Campo               | Tipo    | Descripción                                               |
|--------------------|---------|-----------------------------------------------------------|
| `Código DANE`       | Integer | Identificador único por municipio.                        |
| `Municipio`         | String  | Nombre del municipio.                                     |
| `Departamento`      | String  | Departamento al que pertenece el municipio.               |

---

¿Qué datos se analizan?

Con esta información se pueden responder preguntas como:

- ¿Cuántos municipios hay por departamento?
- ¿Cuál es el nombre de todos los municipios de un departamento específico?
- ¿Qué municipios comienzan con cierta letra o patrón?
- ¿Existen códigos DANE duplicados?
- ¿Hay municipios con errores ortográficos?
- [A futuro] ¿Cómo cruzar estos datos con información demográfica, económica o de salud?

---




