import pytest
import pandas as pd
from dashboard.data_loader import validate_data, DataValidationError
from dashboard.config import REQUIRED_COLUMNS

def test_validate_data_ok():
    """Prueba que un DataFrame válido pase la validación (con min_rows=3)."""
    df = pd.DataFrame({
        "Cluster": [0, 1, 2],
        "Estrato_Categoria": ["Estrato 1", "Estrato 2", "Estrato 1"],
        "P6040": [30, 25, 40],
        "P6020": [1, 2, 1],
        "P1082S2": [1, 2, 1],
        "P1083S5": [0, 0, 1],
        "P1084": [1, 5, 1]
    })
    # Ejecutamos pasando min_rows=3 para que no falle por el umbral real de 100k
    validate_data(df, min_rows=3)

def test_validate_data_empty():
    """Prueba que un DataFrame vacío lance DataValidationError."""
    df = pd.DataFrame()
    with pytest.raises(DataValidationError, match="vacío"):
        validate_data(df)

def test_validate_data_missing_columns():
    """Prueba que falten columnas lance DataValidationError."""
    df = pd.DataFrame({"Cluster": [0], "Estrato_Categoria": ["Estrato 1"]})
    with pytest.raises(DataValidationError, match="Faltan columnas"):
        validate_data(df, min_rows=1)

def test_validate_data_invalid_cluster():
    """Prueba que un clúster no mapeado lance DataValidationError."""
    df = pd.DataFrame({
        "Cluster": [99],
        "Estrato_Categoria": ["Estrato 1"],
        "P6040": [30],
        "P6020": [1],
        "P1082S2": [1],
        "P1083S5": [0],
        "P1084": [1]
    })
    with pytest.raises(DataValidationError, match="Valores inesperados"):
        validate_data(df, min_rows=1)