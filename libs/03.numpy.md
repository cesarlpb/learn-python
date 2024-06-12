# Introducción a NumPy

**Puedes usar un cuaderno de Python para ejecutar los ejemplos de este cuaderno**

## ¿Qué es NumPy?

NumPy (Numerical Python) es una biblioteca fundamental para la computación científica en Python. Proporciona un objeto de matriz multidimensional, varias funciones derivadas, herramientas para integrar C/C++ y Fortran, capacidades de álgebra lineal, generación de números aleatorios y mucho más. NumPy es el núcleo de muchas otras bibliotecas científicas en Python, como SciPy, Pandas y Matplotlib.

## ¿Cuándo se Usa NumPy?

NumPy se utiliza cuando necesitas realizar cálculos numéricos eficientes en Python. Es especialmente útil para operaciones matemáticas y lógicas en grandes conjuntos de datos, manipulaciones de matrices y generación de datos de manera eficiente. Algunas de las tareas comunes que puedes realizar con NumPy incluyen:

- **Creación y Manipulación de Matrices**: Manipular datos en estructuras de matriz N-dimensional.
- **Operaciones Matemáticas y Lógicas**: Realizar operaciones rápidas y eficientes en arreglos y matrices.
- **Estadísticas y Álgebra Lineal**: Realizar cálculos estadísticos y de álgebra lineal.
- **Generación de Datos**: Crear secuencias de datos y números aleatorios.

## Ejemplos de Código con NumPy

### Instalación

Para instalar NumPy, puedes usar pip:

```bash
pip install numpy
```

### Importar la Librería

```python
import numpy as np
```

### Crear Arreglos

#### Crear un Arreglo desde una Lista

```python
import numpy as np

# Crear un arreglo unidimensional
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Crear un arreglo bidimensional
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
```

#### Crear Arreglos Usando Funciones de NumPy

```python
import numpy as np

# Crear un arreglo de ceros
zeros = np.zeros((3, 4))
print(zeros)

# Crear un arreglo de unos
ones = np.ones((2, 3))
print(ones)

# Crear un arreglo con valores aleatorios
random = np.random.random((2, 2))
print(random)

# Crear un arreglo con valores espaciados uniformemente
linspace = np.linspace(0, 10, 5)
print(linspace)
```

### Operaciones Matemáticas Básicas

```python
import numpy as np

# Crear arreglos de ejemplo
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Suma de arreglos
suma = a + b
print(suma)

# Resta de arreglos
resta = a - b
print(resta)

# Producto elemento a elemento
producto = a * b
print(producto)

# División elemento a elemento
division = a / b
print(division)

# Producto punto
producto_punto = np.dot(a, b)
print(producto_punto)
```

### Funciones Universales

```python
import numpy as np

# Crear un arreglo de ejemplo
arr = np.array([0, np.pi/2, np.pi])

# Aplicar funciones trigonométricas
sin = np.sin(arr)
cos = np.cos(arr)
tan = np.tan(arr)

print(sin)
print(cos)
print(tan)
```

### Manipulación de Matrices

#### Redimensionar Matrices

```python
import numpy as np

# Crear un arreglo de ejemplo
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Redimensionar a 3x2
reshaped = arr.reshape((3, 2))
print(reshaped)
```

#### Transponer Matrices

```python
import numpy as np

# Crear un arreglo de ejemplo
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Transponer el arreglo
transposed = arr.T
print(transposed)
```

### Álgebra Lineal

```python
import numpy as np

# Crear una matriz de ejemplo
matrix = np.array([[1, 2], [3, 4]])

# Calcular el determinante
det = np.linalg.det(matrix)
print(det)

# Calcular la inversa
inverse = np.linalg.inv(matrix)
print(inverse)
```

### Estadísticas Básicas

```python
import numpy as np

# Crear un arreglo de ejemplo
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Calcular la media
mean = np.mean(arr)
print(mean)

# Calcular la mediana
median = np.median(arr)
print(median)

# Calcular la desviación estándar
std_dev = np.std(arr)
print(std_dev)
```

## Conclusión

NumPy es una herramienta esencial para la computación científica y el análisis de datos en Python. Su capacidad para manejar operaciones matemáticas y lógicas de manera eficiente lo convierte en la elección ideal para trabajar con grandes conjuntos de datos y realizar cálculos complejos. Con sus poderosas funcionalidades y su integración con otras bibliotecas, NumPy es fundamental para cualquier trabajo de ciencia de datos y análisis numérico en Python.