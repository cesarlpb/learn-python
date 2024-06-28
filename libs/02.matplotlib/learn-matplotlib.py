# Introducción a matplotlib

"""Activando el entorno virtual
  pip install matplotlib
"""
#%% print de la versión
import matplotlib
print(f"Estamos usando matplotlib v.{matplotlib.__version__}")
import matplotlib.pyplot as plt # importación estándar

#%% Gráfico de línea
import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear el gráfico de líneas
plt.plot(x, y)

# Añadir título y etiquetas
plt.title('Gráfico de Líneas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.show()

#%% Gráfico de barras
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

#%% Histograma
import matplotlib.pyplot as plt

# Datos de ejemplo
datos = [1, 2, 2, 3, 3, 4, 4, 4, 4, 5]

# Crear el histograma
plt.hist(datos, bins=5, edgecolor='black') # edgecolor también recibe HEX

# Añadir título y etiquetas
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.show()

#%% Scatter o dispersión
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

#%% Sectores
import matplotlib.pyplot as plt

# Datos de ejemplo
etiquetas = ['Python', 'Javascript', 'C#', 'Java', 'Otros']
tamanos = [33, 30, 17, 10, 10]

# Crear el gráfico de sectores
plt.pie(tamanos, labels=etiquetas, autopct='%1.0f%%', startangle=90)

# Añadir título
plt.title('Lenguajes de Programación más usados')

# Asegurar que el gráfico sea circular
plt.axis('equal')

# Mostrar el gráfico
plt.show()
# %% 3D
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
ax.plot_surface(x, y, z, cmap='inferno') # cmap son códigos de color para añadir a la gráfica https://matplotlib.org/stable/users/explain/colors/colormaps.html

# Añadir título y etiquetas
ax.set_title('Gráfico 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar el gráfico
plt.show()

#%% Ejemplo de benchmark de algoritmos
import timeit
import matplotlib.pyplot as plt
import numpy as np

# Definir las implementaciones del algoritmo
def sum_for_loop(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def sum_builtin(numbers):
    return sum(numbers)

def sum_numpy(numbers):
    return np.sum(numbers)

# Crear una lista de números para la prueba
numbers = list(range(1_000_000))

# Medir los tiempos de ejecución usando timeit
time_for_loop = timeit.timeit('sum_for_loop(numbers)', globals=globals(), number=100)
time_builtin = timeit.timeit('sum_builtin(numbers)', globals=globals(), number=100)
time_numpy = timeit.timeit('sum_numpy(numbers)', globals=globals(), number=100)

# Imprimir los tiempos de ejecución
print(f'Tiempo usando for loop: {time_for_loop:.6f} segundos')
print(f'Tiempo usando sum builtin: {time_builtin:.6f} segundos')
print(f'Tiempo usando numpy: {time_numpy:.6f} segundos')

# Visualizar los resultados con matplotlib
labels = ['For Loop', 'Sum Builtin', 'Numpy']
times = [time_for_loop, time_builtin, time_numpy]

plt.bar(labels, times, color=['#fdba74', '#fb923c', '#f97316']) # admite colore en HEX
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de ejecución de diversas implementaciones')
plt.show()
