# Introducción a Pandas

**Puedes usar un cuaderno de Python para ejecutar los ejemplos de este cuaderno**

## ¿Qué es Pandas?

Pandas es una librería de Python que proporciona estructuras de datos y herramientas de análisis de datos de alto rendimiento y fáciles de usar. Es especialmente útil para manipular y analizar datos en formato tabular, como hojas de cálculo y bases de datos.

Pandas se construye sobre la librería NumPy y está destinada a facilitar el trabajo con datos de series temporales y matrices. Ofrece dos estructuras de datos principales:

- **Series**: Una estructura de datos unidimensional similar a una lista o un array.
- **DataFrame**: Una estructura de datos bidimensional similar a una tabla en una base de datos o una hoja de cálculo.

## ¿Cuándo se Usa Pandas?

Pandas se utiliza cuando necesitas realizar análisis de datos, manipulación de datos y limpieza de datos. Algunas de las tareas comunes que puedes realizar con Pandas incluyen:

- **Lectura y Escritura de Datos**: Importar y exportar datos desde y hacia diversos formatos como CSV, Excel, SQL, JSON, etc.
- **Manipulación de Datos**: Filtrar, agregar, agrupar y transformar datos.
- **Limpieza de Datos**: Manejar datos faltantes, duplicados y realizar transformaciones en los datos.
- **Análisis de Datos**: Realizar cálculos estadísticos y sumarizaciones, generar reportes y gráficos.

## Ejemplos de Código con Pandas

### Instalación

Para instalar Pandas, puedes usar pip:

```bash
pip install pandas
```

### Importar la Librería

```python
import pandas as pd
```

### Creación de una Serie

Una Serie es una estructura de datos unidimensional que puede almacenar cualquier tipo de datos.

```python
import pandas as pd

# Crear una Serie a partir de una lista
data = [1, 2, 3, 4, 5]
serie = pd.Series(data)

print(serie)
```

### Creación de un DataFrame

Un DataFrame es una estructura de datos bidimensional con columnas de potencialmente diferentes tipos.

```python
import pandas as pd

# Crear un DataFrame a partir de un diccionario
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria'],
    'Edad': [28, 24, 22, 32],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}
df = pd.DataFrame(data)

print(df)
```

### Lectura de Datos desde un Archivo CSV

```python
import pandas as pd

# Leer un archivo CSV
df = pd.read_csv('ruta/al/archivo.csv')

print(df.head())  # Mostrar las primeras 5 filas del DataFrame
```

### Escritura de Datos a un Archivo CSV

```python
import pandas as pd

# Suponiendo que df es un DataFrame
df.to_csv('ruta/al/nuevo_archivo.csv', index=False)
```

### Filtrado de Datos

```python
import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria'],
    'Edad': [28, 24, 22, 32],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}
df = pd.DataFrame(data)

# Filtrar filas donde la edad es mayor de 25
df_filtrado = df[df['Edad'] > 25]

print(df_filtrado)
```

### Agrupación y Agregación de Datos

```python
import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria', 'Juan'],
    'Edad': [28, 24, 22, 32, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Madrid']
}
df = pd.DataFrame(data)

# Agrupar por la columna 'Ciudad' y calcular la edad promedio
df_agrupado = df.groupby('Ciudad')['Edad'].mean()

print(df_agrupado)
```

### Manejo de Datos Faltantes

```python
import pandas as pd
import numpy as np

# Crear un DataFrame con valores faltantes
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria'],
    'Edad': [28, np.nan, 22, 32],
    'Ciudad': ['Madrid', 'Barcelona', np.nan, 'Sevilla']
}
df = pd.DataFrame(data)

# Rellenar valores faltantes en la columna 'Edad' con la edad promedio
df['Edad'].fillna(df['Edad'].mean(), inplace=True)

# Eliminar filas con valores faltantes
df.dropna(inplace=True)

print(df)
```

## Conclusión

Pandas es una herramienta poderosa para cualquier analista de datos o científico de datos que trabaje con Python. Facilita la manipulación, análisis y visualización de datos de manera eficiente y eficaz. Con sus extensas capacidades, Pandas se convierte en una opción ideal para tareas de análisis de datos.