# Limitaciones del Estudio

1. **Pérdida de muestra en merge:** Al cruzar con la base de Vivienda (Stata), se perdió el 4.23% de la muestra (7,575 personas) por falta de georreferenciación o estratos especiales (0, 8, 9).
2. **Ausencia de variables geográficas:** El modelo trató el territorio como una bolsa homogénea; no incluyó departamentos o municipios.
3. **Supuestos geométricos:** K-Means asume clústeres esféricos; GMM asume distribuciones gaussianas.
4. **Imputación lógica:** Se asumió que "si no tiene celular, no tiene smartphone ni usa internet". Aunque es el diseño del DANE, es una aproximación.
5. **Etnia excluida del clustering:** Los clústeres no fueron construidos con etnia, solo descritos por ella.