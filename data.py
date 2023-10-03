import pandas as pd
import seaborn as sns


df = pd.read_excel('datos.xlsx')

df.to_csv('datos.csv', index=False)

print(df.head())

# Para analizar las ventas por producto:
ventas_por_producto = df.groupby('Product Name')['Sales'].sum()
sns.barplot(x=ventas_por_producto.index, y=ventas_por_producto.values)

# Para analizar las ventas por cliente:
ventas_por_cliente = df.groupby('Customer Name')['Sales'].sum()
sns.barplot(x=ventas_por_cliente.index, y=ventas_por_cliente.values)

# Para analizar las ventas por región:
ventas_por_region = df.groupby('Region')['Sales'].sum()
sns.barplot(x=ventas_por_region.index, y=ventas_por_region.values)

# Para analizar las ventas por segmento:
ventas_por_segmento = df.groupby('Segment')['Sales'].sum()
sns.barplot(x=ventas_por_segmento.index, y=ventas_por_segmento.values)
