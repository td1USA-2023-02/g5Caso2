import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('datos.xlsx')

df.to_csv('datos.csv', index=False)

print(df.head())

# Obtener información sobre los tipos de datos de cada columna
print(df.dtypes)

# Filtrar las columnas que contienen variables categóricas
categorical_cols = [col for col in df.columns if df[col].dtype == 'object']

# Imprimir las columnas que contienen variables categóricas
print(categorical_cols)

# Filtrar las columnas que contienen variables cuantitativas
quantitative_cols = [col for col in df.columns if df[col].dtype != 'object']

# Imprimir las columnas que contienen variables cuantitativas
print(quantitative_cols)

## ## ##

# Convertir la columna 'Order Date' a datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extraer el año y agregarlo como una nueva columna
df['Year'] = df['Order Date'].dt.year

# Obtener los años únicos en el dataframe
years = df['Year'].unique()

# Crear un nuevo csv para cada año
for year in years:
    df_year = df[df['Year'] == year]
    df_year.to_csv(f'datos_{year}.csv', index=False)

## __________________________________________

# Obtener una lista de todos los valores únicos en la columna "City"
unique_cities = df['City'].unique()

# Imprimir la lista de valores únicos
print(unique_cities)

# Contar la cantidad de veces que aparece cada valor único en la columna "City"
city_counts = df['City'].value_counts()

# Imprimir la cantidad de veces que aparece cada valor único
print(city_counts)

## ___________________________

# Agrupar por 'Region' y contar el número de ventas (filas) en cada región
ventas_por_region = df.groupby('Region').size()

# Ordenar los datos de menor a mayor
ventas_por_region.sort_values(inplace=True)

# Imprimir un resumen en la terminal
print(ventas_por_region)

# Crear un gráfico de líneas
plt.figure(figsize=(10, 6))
ventas_por_region.plot(kind='line', marker='o')
plt.title('Número de ventas por región')
plt.xlabel('Región')
plt.ylabel('Número de ventas')
plt.grid(True)
plt.show()

## __________________________________________________________________________

# Filtrar los datos para los estados mencionados
estados = ['Louisiana', 'South Carolina', 'Mississippi', 'Arkansas', 'Alabama', 
           'Kentucky', 'Tennessee', 'Georgia', 'Virginia', 'North Carolina', 'Florida']
df_south_estados = df_south[df_south['State'].isin(estados)]

# Agrupar por 'City' y contar el número de ventas (filas) en cada ciudad
ventas_por_ciudad = df_south_estados.groupby('City').size()

# Ordenar los datos de menor a mayor
ventas_por_ciudad.sort_values(inplace=True)

# Imprimir un resumen en la terminal
print(ventas_por_ciudad)