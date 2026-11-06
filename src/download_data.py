# src/download_data.py
import requests
import os

def download_file(url, destination_folder):
    """Descarga un archivo desde una URL y lo guarda en la carpeta de destino."""
    os.makedirs(destination_folder, exist_ok=True)
    local_filename = os.path.join(destination_folder, url.split('/')[-1])
    
    # NOTA: Debes obtener la URL directa del archivo desde el portal de ONTIC/DANE.
    # Este es un ejemplo genérico.
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Archivo descargado en: {local_filename}")

if __name__ == "__main__":
    # Reemplaza con las URLs directas de los archivos que encontraste en los catálogos.
    URL_TIC_CSV = "URL_DIRECTA_DEL_ARCHIVO_CSV_DE_ONTIC" 
    URL_VIVIENDA_DTA = "URL_DIRECTA_DEL_ARCHIVO_DTA_DEL_DANE"
    
    print("Iniciando descarga de microdatos...")
    # download_file(URL_TIC_CSV, "data/raw")
    # download_file(URL_VIVIENDA_DTA, "data/raw")
    print("Descarga finalizada. Verifique los archivos en data/raw/")