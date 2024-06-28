# Introducción a Seaborn

**Puedes usar un cuaderno de Python para ejecutar los ejemplos de este cuaderno**

## ¿Qué es Seaborn?

Seaborn es una biblioteca de visualización de datos en Python basada en Matplotlib. Proporciona una interfaz de alto nivel para dibujar gráficos estadísticos atractivos y con estilo. Seaborn hace que sea fácil explorar y comprender los datos, y es especialmente útil para la visualización de datos complejos.

## ¿Cuándo se Usa Seaborn?

Seaborn se utiliza cuando necesitas crear gráficos estadísticos de manera sencilla y efectiva. Algunas de las tareas comunes que puedes realizar con Seaborn incluyen:

- **Visualización de Distribuciones**: Histogramas, KDE (Kernel Density Estimation), etc.
- **Visualización de Relaciones**: Gráficos de dispersión, gráficos de línea, etc.
- **Visualización de Categorizaciones**: Gráficos de barras, gráficos de violín, gráficos de caja, etc.
- **Visualización de Matrices de Correlación**: Mapas de calor, etc.

## Ejemplos de Código con Seaborn

### Instalación

Para instalar Seaborn, puedes usar pip:

```bash
pip install seaborn
```

### Importar la Librería

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

### Visualización de Distribuciones

#### Histograma y KDE

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
data = sns.load_dataset("tips")

# Crear un histograma y KDE
sns.histplot(data['total_bill'], kde=True)

# Añadir título y etiquetas
plt.title('Distribución de Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.show()
```

### Visualización de Relaciones

#### Gráfico de Dispersión

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
data = sns.load_dataset("iris")

# Crear un gráfico de dispersión
sns.scatterplot(x='sepal_length', y='sepal_width', data=data, hue='species')

# Añadir título y etiquetas
plt.title('Relación entre Sepal Length y Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

# Mostrar el gráfico
plt.show()
```

#### Gráfico de Líneas

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
data = sns.load_dataset("flights")

# Crear un gráfico de líneas
sns.lineplot(x='year', y='passengers', data=data)

# Añadir título y etiquetas
plt.title('Pasajeros a lo Largo del Tiempo')
plt.xlabel('Año')
plt.ylabel('Pasajeros')

# Mostrar el gráfico
plt.show()
```

### Visualización de Categorizaciones

#### Gráfico de Barras

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
data = sns.load_dataset("tips")

# Crear un gráfico de barras
sns.barplot(x='day', y='total_bill', data=data)

# Añadir título y etiquetas
plt.title('Total Bill por Día')
plt.xlabel('Día')
plt.ylabel('Total Bill')

# Mostrar el gráfico
plt.show()
```

#### Gráfico de Caja

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
data = sns.load_dataset("tips")

# Crear un gráfico de caja
sns.boxplot(x='day', y='total_bill', data=data)

# Añadir título y etiquetas
plt.title('Distribución de Total Bill por Día')
plt.xlabel('Día')
plt.ylabel('Total Bill')

# Mostrar el gráfico
plt.show()
```

### Visualización de Matrices de Correlación

#### Mapa de Calor

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
data = sns.load_dataset("iris")

# Calcular la matriz de correlación
correlation_matrix = data.corr()

# Crear un mapa de calor
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

# Añadir título
plt.title('Matriz de Correlación de Iris')

# Mostrar el gráfico
plt.show()
```

## Conclusión

Seaborn es una herramienta poderosa para la visualización de datos estadísticos en Python. Su capacidad para generar gráficos informativos y atractivos de manera sencilla lo convierte en una elección ideal para la exploración y presentación de datos. Con su interfaz de alto nivel y su integración con Matplotlib, Seaborn facilita la creación de visualizaciones complejas y estéticamente agradables, permitiendo a los usuarios enfocarse más en el análisis de datos y menos en los detalles de la implementación gráfica.