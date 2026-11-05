# Auditoría de Data Leakage

| Prueba | Implementación | Resultado |
|---|---|---|
| **Independencia Train/Test** | `GroupShuffleSplit` agrupado por `DIRECTORIO`. | Intersección de hogares = 0. |
| **Escalado Z-score** | `StandardScaler.fit()` solo en Train, `transform()` en Test. | Media Train = 0, Std Train = 1. |
| **Separación Perfecta** | Exclusión de `P1082` (Tiene celular) en Regresión Logística. | Evita coeficientes infinitos al predecir banca. |
| **Hold-out Externo** | Evaluación del Random Forest en `df_test_external.csv` (44,702 registros no vistos por K-Means). | Métricas honestas, sin sobreajuste. |