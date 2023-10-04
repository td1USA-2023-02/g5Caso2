import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('g5Caso2/datos.xlsx')

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

# Crear un gráfico de barras que muestre la cantidad de ventas por ciudad
## sns.barplot(x='City', y='Sales', data=df)

# Mostrar el gráfico
## plt.show()

# Obtener una lista de todos los valores únicos en la columna "City"
unique_cities = df['City'].unique()

# Imprimir la lista de valores únicos
print(unique_cities)

# Contar la cantidad de veces que aparece cada valor único en la columna "City"
city_counts = df['City'].value_counts()

# Imprimir la cantidad de veces que aparece cada valor único
print(city_counts)

# Filtrar las filas que corresponden a las ciudades que deseas incluir en el gráfico
cities = ['New York City', 'Los Angeles', 'Philadelphia', 'San Francisco', 'Seattle']
df_filtered = df[df['City'].isin(cities)]

# Crear un gráfico de barras que muestre las ventas por ciudad
sns.barplot(x='City', y='Sales', data=df_filtered)

# Mostrar el gráfico
plt.show()

# Crear un gráfico de líneas que muestre las ventas por ciudad
sns.lineplot(x='City', y='Sales', data=df_filtered, sort=False, marker='o')

# Mostrar el gráfico
plt.show()