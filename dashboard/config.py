from pathlib import Path

# Ruta raíz del proyecto (dos niveles arriba desde dashboard/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "dataset_perfilado.csv"

# Mapeo de clústeres a nombres legibles para la interfaz
CLUSTER_NAMES = {
    0: "Mayores Básicos",
    1: "Mujeres Conectadas",
    2: "Hombres Excluidos",
    3: "Élite Digital",
    4: "Hombres Conectados",
    5: "Mujeres Excluidas",
}

# Columnas mínimas requeridas para que el dashboard funcione
REQUIRED_COLUMNS = [
    "Cluster", "Estrato_Categoria", "P6040", "P6020",
    "P1082S2", "P1083S5", "P1084"
]

# Umbral de aceptación para la validación de datos
MIN_ROWS = 100_000  # El dataset original tiene ~178,993 filas