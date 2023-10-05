import pandas as pd
import matplotlib.pyplot as plt

# Lista de años para los que se tienen datos
years = range(2014, 2018)

for year in years:
    # Cargar el dataframe
    df = pd.read_csv(f'datos_{year}.csv')

    # Agrupar por 'Region' y contar el número de ventas (filas) en cada región
    ventas_por_region = df.groupby('Region').size()

    # Ordenar los datos de menor a mayor
    ventas_por_region.sort_values(inplace=True)

    # Imprimir un resumen en la terminal
    print(f'Ventas por región para el año {year}:')
    print(ventas_por_region)

    # Crear un gráfico de líneas
    plt.figure(figsize=(10, 6))
    ventas_por_region.plot(kind='line', marker='o')
    plt.title(f'Número de ventas por región para el año {year}')
    plt.xlabel('Región')
    plt.ylabel('Número de ventas')
    plt.grid(True)
    plt.show()

## _______________________________________________ ##

# Agrupar por 'State' y contar el número de ventas (filas) en cada estado
    # Filtrar los datos para la región 'South'
    df_south = df[df['Region'] == 'South']

    ventas_por_estado = df_south.groupby('State').size()

    # Ordenar los datos de menor a mayor
    ventas_por_estado.sort_values(inplace=True)

    # Imprimir un resumen en la terminal
    print(f'Ventas por estado en la región Sur para el año {year}:')
    print(ventas_por_estado)

    # Crear un gráfico de líneas
    plt.figure(figsize=(10, 6))
    ventas_por_estado.plot(kind='line', marker='o')
    plt.title(f'Número de ventas por estado en la región Sur para el año {year}')
    plt.xlabel('Estado')
    plt.ylabel('Número de ventas')
    plt.grid(True)
    plt.show()

    ## ____________________________________________________ ## 



# Cargar el dataframe
df = pd.read_csv('datos.csv')

# Agrupar por 'Region' y contar el número de ventas (filas) en cada región
ventas_por_region = df.groupby('Region').size()

# Identificar la región con el mayor y el menor número de ventas
region_max_ventas = ventas_por_region.idxmax()
region_min_ventas = ventas_por_region.idxmin()

# Filtrar los datos para las regiones identificadas
df_max_ventas = df[df['Region'] == region_max_ventas]
df_min_ventas = df[df['Region'] == region_min_ventas]

# Analizar las variables para cada región
variables = ['Ship Mode', 'Segment', 'City', 'State', 'Category', 'Sub-Category', 'Discount', 'Profit', 'Status']
for var in variables:
    print(f'Análisis para la variable {var}:')
    
    # Crear una figura con dos subgráficos
    fig, axs = plt.subplots(1, 2, figsize=(10, 6))
    
    # Graficar los datos para la región con el mayor número de ventas
    df_max_ventas[var].value_counts().plot(kind='bar', ax=axs[0])
    axs[0].set_title(f'Región con el mayor número de ventas: {region_max_ventas}')
    
    # Graficar los datos para la región con el menor número de ventas
    df_min_ventas[var].value_counts().plot(kind='bar', ax=axs[1])
    axs[1].set_title(f'Región con el menor número de ventas: {region_min_ventas}')
    
    # Mostrar la figura
    plt.tight_layout()
    plt.show()
