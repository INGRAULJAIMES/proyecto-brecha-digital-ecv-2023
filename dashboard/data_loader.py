import logging
import pandas as pd
import streamlit as st
from dashboard.config import DATA_PATH, REQUIRED_COLUMNS, MIN_ROWS, CLUSTER_NAMES

# Configuración de logging (visible en los logs de Streamlit Cloud)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class DataValidationError(Exception):
    """Excepción personalizada para errores de validación de datos."""
    pass

@st.cache_data(ttl=3600, show_spinner="Cargando datos de perfiles...")
def load_data(file_path: str = str(DATA_PATH)) -> pd.DataFrame:
    """Carga el dataset perfilado desde un archivo CSV con caché de 1 hora."""
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas.")
        return df
    except FileNotFoundError:
        logger.error(f"Archivo no encontrado: {file_path}")
        raise DataValidationError(
            f"No se encontró el archivo en {file_path}. "
            "Asegúrate de que el pipeline de preparación se haya ejecutado."
        )
    except pd.errors.EmptyDataError:
        logger.error("El archivo CSV está vacío.")
        raise DataValidationError("El archivo de datos está vacío. Verifica el pipeline.")
    except Exception as e:
        logger.exception("Error inesperado al cargar el archivo.")
        raise DataValidationError(f"Error inesperado al cargar los datos: {str(e)}")

def validate_data(df: pd.DataFrame, min_rows: int = MIN_ROWS) -> None:
    """Valida la integridad del DataFrame. Lanza DataValidationError si falla."""
    if df.empty:
        raise DataValidationError("El DataFrame está vacío.")

    if len(df) < min_rows:
        raise DataValidationError(
            f"El dataset tiene {len(df)} filas, pero se esperaban al menos {min_rows}. "
            "El archivo puede estar corrupto o incompleto."
        )

    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise DataValidationError(
            f"Faltan columnas requeridas: {missing_cols}. Revisa el notebook de perfilamiento."
        )

    expected_clusters = set(CLUSTER_NAMES.keys())
    actual_clusters = set(df["Cluster"].dropna().unique())
    if not actual_clusters.issubset(expected_clusters):
        raise DataValidationError(
            f"Valores inesperados en 'Cluster': {actual_clusters - expected_clusters}. "
            "El mapeo de clústeres puede estar desactualizado."
        )

    critical_cols = ["Cluster", "Estrato_Categoria", "P6040", "P6020"]
    for col in critical_cols:
        if df[col].isnull().any():
            raise DataValidationError(f"La columna crítica '{col}' contiene valores nulos.")

    logger.info("Validación de datos completada sin errores.")

def get_validated_data() -> pd.DataFrame:
    """Punto de entrada único para obtener datos listos para la interfaz."""
    df = load_data()
    validate_data(df)

    # Enriquecimiento: añadir nombre legible del clúster
    df["Cluster_Nombre"] = df["Cluster"].map(CLUSTER_NAMES)

    if df["Cluster_Nombre"].isnull().any():
        missing_ids = df[df["Cluster_Nombre"].isnull()]["Cluster"].unique()
        raise DataValidationError(
            f"Clústeres sin nombre en el mapeo: {missing_ids}. Revisa config.py."
        )

    return df