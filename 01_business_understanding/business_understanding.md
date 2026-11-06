@'
# 1.1 Contexto del Problema y Justificación

## La Falacia del Estrato
La política pública colombiana de inclusión digital y financiera asigna recursos basándose en la vulnerabilidad económica (Estrato 1 y 2). Este enfoque asume erróneamente que **pobreza económica equivale a exclusión digital**.

## Consecuencias de la Focalización Actual
1. **Fuga de Recursos (Error Tipo I):** Se subsidia conectividad a personas de Estrato 1 que ya cuentan con Smartphone y usan banca digital (Clúster 3).
2. **Exclusión Profunda (Error Tipo II):** Se ignora a poblaciones sin energía eléctrica o sin hardware, para quienes un subsidio de datos móviles es inútil (Clústeres 2 y 5).

## Justificación del Machine Learning
Los métodos tradicionales (reglas de negocio, cruces de variables) son insuficientes para capturar la naturaleza multidimensional de la brecha. El uso de **Clustering No Supervisado** permite descubrir perfiles latentes basados en el comportamiento digital real, no en supuestos demográficos.
'@ | Out-File -FilePath 01_business_understanding/01_contexto_problema.md -Encoding utf8

@'
# 1.2 Objetivos SMART y KPIs de Éxito

## Objetivo General
Identificar perfiles de inclusión digital mediante Machine Learning para reemplazar la focalización por estrato por una **Focalización Multidimensional**.

## Objetivos Específicos (SMART)
1. **Segmentar:** Descubrir empíricamente el número óptimo de clústeres (K) que expliquen la varianza del comportamiento digital en la ECV 2023.
2. **Validar:** Demostrar estadísticamente que la demografía (Estrato, Edad, Sexo) no puede predecir el clúster de un individuo (Validación Negativa).
3. **Cuantificar:** Estimar el impacto del hardware (Smartphone) en la probabilidad de inclusión financiera mediante Odds Ratios.

## KPIs del Proyecto (Criterios de Éxito)
| KPI | Métrica | Umbral Esperado |
|---|---|---|
| **Estabilidad del Modelo** | Adjusted Rand Index (Bootstrap) | ≥ 0.75 |
| **Consistencia Algorítmica** | ARI (K-Means vs GMM) | ≥ 0.70 |
| **Accionabilidad de Política** | Tamaño mínimo de clúster | ≥ 5% de la población |
| **Poder Explicativo** | F1-Macro del Random Forest (Demografía) | ≤ 0.60 (Demuestra que el clustering es necesario) |
'@ | Out-File -FilePath 01_business_understanding/02_objetivos_kpis.md -Encoding utf8

@'
# 1.3 Mapa de Stakeholders

| Stakeholder | Rol | Interés en el Proyecto |
|---|---|---|
| **Ministerio de las TIC** | Diseñador de Política Pública | Optimizar la asignación de recursos del Fondo Único de TIC. |
| **Banca de las Oportunidades** | Promotor Financiero | Identificar barreras de adopción de banca digital (confianza vs. hardware). |
| **DANE** | Proveedor de Datos | Uso secundario de la ECV 2023 para generar valor público. |
| **Población Vulnerable** | Beneficiario Final | Recibir la herramienta exacta que necesita (energía, hardware o educación). |
'@ | Out-File -FilePath 01_business_understanding/03_stakeholders.md -Encoding utf8