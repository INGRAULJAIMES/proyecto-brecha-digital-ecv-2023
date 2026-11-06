# Datos Crudos (Raw Data) - Instrucciones

Esta carpeta está destinada a almacenar los microdatos originales del DANE. **Estos archivos no se versionan en Git** por su tamaño y para evitar la duplicación de datos oficiales.

## ¿Cómo obtenerlos?

Sigue las instrucciones detalladas en el documento de procedencia: **[docs/data_sources.md](../../docs/data_sources.md)**.

**Resumen rápido:**
1.  **Archivo de Personas/Hogares (TIC):** Descarga `Caracteristicas Hogar y Tenencia TIC ECV 2023.csv` desde el [Catálogo de ONTIC](https://ontic.mintic.gov.co/857/w3-propertyvalue-916080.html).
2.  **Archivo de Vivienda (Estrato):** Descarga el archivo `.DTA` del módulo de Vivienda desde el [Catálogo del DANE](https://microdatos.dane.gov.co/index.php/catalog/827/get-microdata).

Una vez descargados, colócalos directamente en esta carpeta (`data/raw/`). El notebook `03_data_preparation/01_limpieza.ipynb` está configurado para leerlos desde aquí.