# Reporte de Evaluación

## Validación Supervisada (Random Forest)
- **F1-Macro:** 0.52
- **Interpretación:** Validación negativa exitosa. El modelo intentó predecir los clústeres usando solo demografía (Estrato, Edad, Sexo, Etnia). Al fallar, demuestra que el comportamiento digital es una dimensión latente que la demografía no puede explicar. Si el F1 fuera >0.90, el clustering habría sido redundante.
- **Clúster 3 (Élite Digital):** F1 = 0.00. La demografía es ciega a la élite digital (pueden ser jóvenes de estrato 1 o adultos de estrato 3).

## Regresión Logística (Odds Ratios)
- **Smartphone (OR = 64.10):** Multiplica por 64 las probabilidades de usar banca digital (IC 95%: 55.93 - 73.47).
- **Mujer (OR = 0.85):** Reduce las probabilidades de usar banca en un 15% a igual estrato y hardware.
- **Pseudo-R² de McFadden:** 0.166. La demografía y el hardware explican solo el 16.6% de la varianza. El 83.4% restante es comportamiento no observado (confianza, educación).