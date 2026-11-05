# Decisiones de Modelado

1. **Exclusión de Etnia en PCA:** Se excluyó la variable `P6080` del PCA para evitar que las minorías demográficas (con alta varianza pero baja frecuencia) secuestraran los componentes principales. Se usó post-hoc para perfilamiento.
2. **Selección de K=6:** Se evaluaron K=2 a K=12. Se aplicó un filtro de accionabilidad (mínimo 5% de la población por clúster). K=6 ganó el score de consenso multivariado (1º en Silhouette 0.6505, 1º en Calinski-Harabasz, 2º en Davies-Bouldin).
3. **Validación de Estabilidad:** Se usaron 20 iteraciones Bootstrap con ARI (Adjusted Rand Index). Resultado: 0.9254 (altamente estable, no depende de la semilla).
4. **Isolation Forest:** Se usó `contamination=0.05` para detectar individuos con combinaciones atípicas (ej. sin celular pero con banca digital).