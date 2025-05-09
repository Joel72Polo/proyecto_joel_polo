# proyecto_joel_polo
Proyecto para consumir datos abiertos de Colombia con patrón MVC

## Objetivo
Crear una aplicación en Python que:
- Consuma datos desde una API pública de datos.gov.co.
- Almacene esos datos en una base de datos.
- Permita operaciones CRUD desde una interfaz de línea de comandos (CLI).
- Siga el patrón de diseño MVC (Modelo - Vista - Controlador).

## Estructura del Proyecto

proyecto_joel_polo/
│
├── app/
│ ├── controllers/ # Lógica de negocio (Controladores)
│ ├── models/ # Modelos y acceso a datos (DAO)
│ ├── views/ # Interfaz CLI
│ └── services/ # API y DB
│
├── database/ # Scripts SQL y migraciones
├── tests/ # Pruebas unitarias
├── requirements.txt # Dependencias
└── README.md # Este archivo

### Fuente de datos

Usaremos el conjunto de datos **Departamentos y Municipios de Colombia**, disponible en:

[https://www.datos.gov.co/Geograf-a-y-Cartograf-a/Departamentos-y-Municipios-de-Colombia/95jt-2v3q](https://www.datos.gov.co/Geograf-a-y-Cartograf-a/Departamentos-y-Municipios-de-Colombia/95jt-2v3q)

Este dataset contiene información sobre los municipios, sus respectivos departamentos y códigos DANE.

## Estado del proyecto

Diseño inicial y conexión con API (Etapa 1)

