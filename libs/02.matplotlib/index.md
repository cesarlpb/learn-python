# Introducción a Matplotlib

**Puedes usar un cuaderno de Python para ejecutar los ejemplos de este cuaderno**

## ¿Qué es Matplotlib?

Matplotlib es una biblioteca de visualización de datos en Python. Es muy utilizada para crear gráficos estáticos, animados e interactivos de manera fácil y rápida. Matplotlib es conocida por su capacidad para generar gráficos de alta calidad, similares a los que se pueden crear con herramientas como MATLAB.

## ¿Cuándo se Usa Matplotlib?

Matplotlib se utiliza cuando necesitas visualizar datos de manera gráfica para entender mejor las tendencias, patrones y relaciones en los datos. Algunas de las tareas comunes que puedes realizar con Matplotlib incluyen:

- **Gráficos de Líneas**: Para visualizar datos continuos a lo largo de un intervalo.
- **Gráficos de Barras**: Para comparar cantidades entre diferentes grupos.
- **Histogramas**: Para mostrar la distribución de un conjunto de datos.
- **Gráficos de Dispersión**: Para mostrar la relación entre dos variables.
- **Gráficos de Sectores**: Para mostrar proporciones de un todo.
- **Gráficos 3D**: Para representar datos en tres dimensiones.

## Ejemplos de Código con Matplotlib

### Instalación

Para instalar Matplotlib, puedes usar pip:

```bash
pip install matplotlib
```

### Importar la Librería

```python
import matplotlib.pyplot as plt
```

### Crear un Gráfico de Líneas

```python
import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear el gráfico de líneas
plt.plot(x, y)

# Añadir título y etiquetas
plt.title('Gráfico de Líneas')
plt.xlabel('X')
plt.ylabel('Y')

# Mostrar el gráfico
plt.show()
```

### Crear un Gráfico de Barras

```python
import matplotlib.pyplot as plt

# Datos de ejemplo
categorias = ['A', 'B', 'C', 'D']
valores = [5, 7, 3, 8]

# Crear el gráfico de barras
plt.bar(categorias, valores)

# Añadir título y etiquetas
plt.title('Gráfico de Barras')
plt.xlabel('Categorías')
plt.ylabel('Valores')

# Mostrar el gráfico
plt.show()
```

### Crear un Histograma

```python
import matplotlib.pyplot as plt

# Datos de ejemplo
datos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Crear el histograma
plt.hist(datos, bins=5, edgecolor='black')

# Añadir título y etiquetas
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.show()
```

### Crear un Gráfico de Dispersión

```python
import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear el gráfico de dispersión
plt.scatter(x, y)

# Añadir título y etiquetas
plt.title('Gráfico de Dispersión')
plt.xlabel('X')
plt.ylabel('Y')

# Mostrar el gráfico
plt.show()
```

### Crear un Gráfico de Sectores

```python
import matplotlib.pyplot as plt

# Datos de ejemplo
etiquetas = ['A', 'B', 'C', 'D']
tamanos = [15, 30, 45, 10]

# Crear el gráfico de sectores
plt.pie(tamanos, labels=etiquetas, autopct='%1.1f%%', startangle=90)

# Añadir título
plt.title('Gráfico de Sectores')

# Asegurar que el gráfico sea circular
plt.axis('equal')

# Mostrar el gráfico
plt.show()
```

### Crear un Gráfico 3D

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Datos de ejemplo
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Crear la figura y el gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear el gráfico de superficie
ax.plot_surface(x, y, z, cmap='viridis')

# Añadir título y etiquetas
ax.set_title('Gráfico 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar el gráfico
plt.show()
```

## Conclusión

Matplotlib es una herramienta poderosa para visualizar datos en Python. Su amplia gama de capacidades de gráficos permite a los usuarios crear visualizaciones efectivas y significativas. Desde gráficos de líneas simples hasta complejas visualizaciones en 3D, Matplotlib proporciona las herramientas necesarias para entender y comunicar mejor tus datos.