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

# Crear un gráfico de dispersión que muestre la relación entre las ventas y el descuento
sns.scatterplot(x='Discount', y='Sales', data=df)

# Mostrar el gráfico
plt.show()