# Fuentes de Datos y Procedencia

Este documento detalla el origen, la fecha de acceso y las condiciones de uso de los microdatos utilizados en el proyecto.

| Conjunto de Datos | Fuente | Año | Archivos Utilizados | URL de Acceso | Fecha de Acceso | Tipo de Acceso | Licencia |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Características del Hogar y Tenencia TIC (ECV)** | DANE / MinTIC (ONTIC) | 2023 | `Caracteristicas Hogar y Tenencia TIC ECV 2023.csv` | [Catálogo ONTIC](https://ontic.mintic.gov.co/857/w3-propertyvalue-916080.html) | Noviembre 2026 | Abierto - Público | Uso público (Ley 1712 de 2014) |
| **Base de Vivienda (ECV)** | DANE | 2023 | Archivo `.DTA` (módulo de Vivienda) | [Catálogo ANDA - DANE](https://microdatos.dane.gov.co/index.php/catalog/827/get-microdata) | Noviembre 2026 | Abierto - Público | Uso público (DANE) |

> **Nota sobre la integración:** Los datos de Tenencia TIC (personas) y la Base de Vivienda se unen a nivel de hogar utilizando la llave `DIRECTORIO`, tal como se especifica en la metodología del proyecto.