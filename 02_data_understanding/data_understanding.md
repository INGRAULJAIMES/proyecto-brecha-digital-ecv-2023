@'
# 2.1 Fuente de Datos y Selección de Variables

## La Fuente
- **Encuesta:** Calidad de Vida (ECV) 2023.
- **Entidad:** Departamento Administrativo Nacional de Estadística (DANE).
- **Universo Inicial:** 240,212 registros, 143 columnas.

## La Reducción Dimensional (De 143 a 11 Variables)
Se descartaron 132 columnas (salud, gastos, educación) para evitar la **maldición de la dimensionalidad** y garantizar que el algoritmo de clustering se enfoque exclusivamente en la brecha digital.

### Variables Retenidas (Comportamiento Digital)
- `P1082`: Tenencia de celular.
- `P1082S2`: Tenencia de Smartphone.
- `P1084`: Frecuencia de uso de Internet.
- `P1083S5`: Uso de banca electrónica.
- `P1083S4`: Compras online.

### Variables de Control (Demografía - Uso Post-Hoc)
- `P6020`: Sexo. | `P6040`: Edad. | `P6080`: Etnia. | `P8520S1A1`: Estrato.
*(Excluidas del PCA para evitar sesgo, usadas para perfilamiento).*
'@ | Out-File -FilePath 02_data_understanding/01_fuente_y_variables.md -Encoding utf8

@'
# 2.2 Diagnóstico de Calidad y Lógica de Salto

## El Fenómeno de "Missing by Design" (Skip Logic)
El DANE aplica Lógica de Salto: si un individuo no posee celular, las preguntas sobre smartphone e internet no se realizan.

| Variable | Nulos Detectados | Diagnóstico |
|---|---|---|
| `P1082` (Celular) | 16,517 | Niños menores de 5 años (Missing by Design). |
| `P1083S5` (Banca) | 218,040 | No se pregunta a quienes no usan internet. |

## Tratamiento Aplicado
1. **Filtro Etario:** Se eliminaron los 16,517 registros de menores de 5 años.
2. **Imputación Jerárquica (Rescate de Desconectados):** Si `P1082 == 2` (No tiene celular), se imputó automáticamente "No tiene smartphone" y "No usa internet".
3. **Códigos Especiales (Estrato):** Se preservaron los códigos 0 (Pirata), 8 (Planta Eléctrica) y 9 (No Responde) como categorías explícitas para no ocultar la ruralidad extrema.
'@ | Out-File -FilePath 02_data_understanding/02_diagnostico_calidad.md -Encoding utf8

@'
# 2.3 Análisis Exploratorio y Anti-Data Leakage

## El Problema del Sesgo por Conglomerados
La ECV utiliza un muestreo por conglomerados (hogares). Si se divide aleatoriamente a nivel de persona, miembros de una misma familia (que comparten estrato y conectividad) terminarían en Train y Test simultáneamente.

## Solución: GroupShuffleSplit
Se utilizó `GroupShuffleSplit` agrupando por la llave `DIRECTORIO`.
- **Resultado:** 178,993 personas en Train (80%) y 44,702 en Test (20%).
- **Auditoría:** Intersección de hogares entre Train y Test = **0**. (Fuga de información eliminada).

## Escalado Z-Score
Se aplicó `StandardScaler`. El `fit()` se ejecutó **exclusivamente** en el conjunto de Train para evitar que la media y desviación estándar del Test (futuro) filtraran información al modelo.
'@ | Out-File -FilePath 02_data_understanding/03_eda_anti_leakage.md -Encoding utf8

