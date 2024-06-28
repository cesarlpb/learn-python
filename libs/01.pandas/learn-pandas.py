# Cuaderno introductorio para aprender de la libería Pandas
"""
  Activando el entorno virtual:
  pip install --upgrade pip
  pip install pandas
"""
#%% Esto es una celda de ejemplo
print("Introducción a Pandas")
import pandas as pd # si os sale warning: which python3 y seleccionais el entorno virtual en VS Code 
print(f"Estamos usando pandas v.{pd.__version__}") 

"""Si os sale un aviso de ipykernel o similar para instalar paquetes de 'kernel' Aceptamos, son necesarios para que el cuaderno funcione en VS Code"""

# %% Series
import pandas as pd

# Crear una Serie a partir de una lista
data = [1, 2, 3, 4, 5]  # lista
serie = pd.Series(data) # serie

print("lista:")
print(data)
print("")
print("serie:")
print(serie)

#%% Comparación en memoria:
import sys

print("lista:", sys.getsizeof(data), "bytes")
print("serie:", sys.getsizeof(serie), "bytes")


# %% Dataframe:
import pandas as pd

# Crear un DataFrame a partir de un diccionario
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria'],
    'Edad': [28, 24, 22, 32],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}
df = pd.DataFrame(data)

print("dict:")
print(data)
print("")
print("dataframe:") # dataframe == df
print(df)

#%% Comparación en memoria:
import sys

print("dict:", sys.getsizeof(data), "bytes")
print("df:", sys.getsizeof(df), "bytes")

"""
Para continuar, buscad un dataset, nos vale cualquiera. 
Yo uso este: https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data (1.45Gb)
""" 

# Para ejecutar la siguiente celda se necesita tener el dataset en la misma carpeta

#%% vehicles.csv
import pandas as pd

# Leer un archivo CSV
df = pd.read_csv('vehicles.csv')

print(df.head())  # Mostrar las primeras 5 filas del DataFrame
#%% Comparación en memoria:
import sys

print("df:", sys.getsizeof(df), "bytes")
print(f"Equivale a {sys.getsizeof(df) / 1_000_000_000} Gb")

#%% Accedemos a una columna por nombre -> Serie
region_col = df['region']
print(region_col)
#%% Accedemos a la primera fila -> Serie
"""La primera fila contiene los nombres de columnas del df:"""

primera_fila = df.iloc[0]
print("primera fila:")
print("")
print(primera_fila) # columnas

# El df tiene campo columns:
print(df.columns)   # columnas

segunda_fila = df.iloc[1]
print("segunda fila:")
print("")
print(segunda_fila) # tengo columnas y valores

# Puedo acceder por nombre de col en la fila:
segundo_id = segunda_fila['id']
print("id:", segundo_id)