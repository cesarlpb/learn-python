## Ejercicios de Librerías

## Indicaciones
Para resolver cada apartado se debe crear un archivo, p.e. `ejercicio_1.py` con el nombre del ejercicio y en cada archivo debe haber un `main()` que se ejecuta con `python <nombre_de_archivo>.py`.

### Ejercicio 1: Comparación de Memoria y Tiempos de Ejecución entre Listas y np.arrays
**Enunciado:**
Crea un programa en Python que compare el uso de memoria y los tiempos de ejecución de diversas operaciones entre listas y np.arrays. Debes realizar las siguientes operaciones:
- Creación de una lista y un np.array con 1 millón de elementos.
- Iteración sobre los elementos para realizar una suma.
- Multiplicación de cada elemento por una constante.

El programa debe imprimir los resultados de uso de memoria y tiempos de ejecución para cada operación.

**Pistas:**
- Usa el módulo `time` para medir los tiempos de ejecución.
- Usa el módulo `sys` para medir el uso de memoria de las estructuras de datos.
- Utiliza funciones de Numpy para las operaciones en np.array y compararlas con las operaciones en listas.

### Ejercicio 2: Visualización de Datos con Matplotlib y Pandas
**Enunciado:**
Crea un programa en Python que genere varias gráficas a partir de un conjunto de datos. Puedes usar un dataset de alturas y pesos de personas, categorizados por edad y género. Debes crear las siguientes gráficas:
- Histograma de alturas.
- Diagrama de dispersión (scatter plot) de pesos vs edades.
- Gráfica de barras (bar plot) de promedios de altura por género.

El programa debe mostrar cada gráfica y permitir la comparación visual de los datos.

**Pistas:**
- Usa Pandas para manipular el dataset.
- Usa Matplotlib para crear las gráficas.
- Asegúrate de etiquetar adecuadamente los ejes y agregar títulos a las gráficas.

### Ejercicio 3: Modelo de Regresión Lineal para Conversión de Temperaturas
**Enunciado:**
Dada una lista de temperaturas en grados Celsius y su correspondiente lista de temperaturas en grados Fahrenheit, crea un modelo de regresión lineal que prediga con una precisión de al menos el 5% la conversión de Celsius a Fahrenheit. Debes:
- Dividir los datos en conjuntos de entrenamiento y prueba.
- Entrenar el modelo usando scikit-learn.
- Evaluar la precisión del modelo en el conjunto de prueba.
- Visualizar los resultados de la predicción comparando las temperaturas reales y las predichas.

El programa debe mostrar la ecuación del modelo y un gráfico de las predicciones vs los valores reales.

**Pistas:**
- Usa scikit-learn para crear y entrenar el modelo de regresión lineal.
- Divide los datos usando `train_test_split` de scikit-learn.
- Evalúa el modelo usando métricas de error y asegúrate de que la precisión esté dentro del 5%.
- Utiliza Matplotlib para graficar las predicciones vs los valores reales.
