# Diccionario de Datos (ECV 2023 - DANE)

## Variables Retenidas (11 de 143 originales)
| Variable DANE | Nombre Descriptivo | Tipo | Tratamiento |
|---|---|---|---|
| `P1082` | Tenencia de celular | Binaria (1=Sí, 2=No) | Mapeo a 1/0 |
| `P1082S2` | Tenencia de Smartphone | Binaria (1=Sí, 2=No) | Mapeo a 1/0 |
| `P1084` | Frecuencia de uso de Internet | Ordinal (1-5) | Escalado Z-score |
| `P1083S5` | Uso de Banca Electrónica | Binaria (1=Sí, NaN=No) | Imputación lógica (NaN=0) |
| `P1083S4` | Compras online | Binaria (1=Sí, NaN=No) | Imputación lógica (NaN=0) |
| `P6020` | Sexo | Categórica (1=Hombre, 2=Mujer) | Mapeo a 0/1 |
| `P6040` | Edad | Continua | Filtro >= 5 años |
| `P6080` | Etnia | Categórica (1-6) | Dummies (excluida en PCA) |
| `DIRECTORIO` | ID de Hogar | Llave | GroupShuffleSplit |
| `SECUENCIA_P` | ID de Persona | Llave | - |
| `ORDEN` | Orden en el hogar | Llave | - |

## Códigos Especiales (Estrato)
- `0`: Sin Estrato / Servicio Pirata
- `8`: Vivienda con Planta Eléctrica (Ruralidad extrema)
- `9`: No Responde / Sin Recibo
*(Tratados como categorías explícitas en la fase de perfilamiento para no perder información).*