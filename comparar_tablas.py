import pandas as pd  # Importa la biblioteca pandas

# Cargar el archivo de Excel
archivo_excel = r'D:\indices-peru-chile.xlsx'

# Leer las hojas de Excel (Peru y Chile)
tabla_peru = pd.read_excel(archivo_excel, sheet_name='PERU')
tabla_chile = pd.read_excel(archivo_excel, sheet_name='CHILE')

# Especifica la columna que quieres comparar
columna_comparar = 'indexname'

# Obtener los registros que están en PERU pero no en CHILE
faltantes_en_chile = tabla_peru[~tabla_peru[columna_comparar].isin(tabla_chile[columna_comparar])]

# Obtener los registros que están en CHILE pero no en PERU
faltantes_en_peru = tabla_chile[~tabla_chile[columna_comparar].isin(tabla_peru[columna_comparar])]

# Imprimir resultados
print("Registros que están en PERU pero no en CHILE:")
print(faltantes_en_chile[[columna_comparar]])  # Muestra solo la columna de índices faltantes en CHILE
print("\nRegistros que están en CHILE pero no en PERU:")
print(faltantes_en_peru[[columna_comparar]])  # Muestra solo la columna de índices faltantes en PERU

# Si deseas incluir más columnas en el resultado, puedes agregar las columnas necesarias en los corchetes
