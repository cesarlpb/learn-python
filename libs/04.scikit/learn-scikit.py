#%%
# %% importación estándar
import sklearn
print("Estamos usando scikit-learn v", sklearn.__version__)

#%% importaciones
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

print("Se han cargado las importaciones")

#%% Cargar el dataset de Iris
iris = datasets.load_iris()
X = iris.data
y = iris.target
print("shape de X:    ", len(X))
print("Elementos en y:", len(y))

#%% split de train y test
# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("Elementos de X_train:", len(X_train))
print("Elementos en y_train:", len(y_train))

print("Elementos de X_test:", len(X_test))
print("Elementos en y_test:", len(y_test))

# test_size == en tanto por uno, el tamaño porcentual de la muestra -> 0.3 -> 30%
# random_state == "identificador" de cómo desordenas los datos inicialmente para que puedas reproducir el experimento

# %% Estandarizar las características => escalado
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("X_train:   ", len(X_train), X_train.shape)
print("X_test:    ", len(X_test), X_test.shape)

# %% Ajuste con 3 vecinos más cercanos
# Entrenar el modelo K-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# %% Predicciones y comparación con test
y_pred = knn.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión: {accuracy:.2f}') # el máximo es 1 en corr positiva y -1 en corr negativa

# si sale 0 o cercano => es una nube de puntos que no tiene correlación como una línea o curva
#%% 
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generar datos de entrenamiento
np.random.seed(0)  # El id para reproducibilidad

# Ejemplo con varios datos:
# celsius = np.array([[-30], [-20], [-10], [0], [10], [20], [30], [40], [50], [60], [70], [80], [90], [100]])
# fahrenheit = celsius * 9 / 5 + 32 # cálculo exacto

# Ejemplo con dos datos:
x = np.array([[-40], [100]])  # etc...
y = np.array([[-38], [198]]) # etc...

celsius = x
fahrenheit = y

# Agregar ruido aleatorio a los datos de Fahrenheit
ruido = np.random.normal(0, 2, fahrenheit.shape)
fahrenheit_con_ruido = fahrenheit + 0.0*ruido # colocando 0 anulamos ruido

# Crear el modelo de regresión lineal
model = LinearRegression()

# Ajustar el modelo con los datos
model.fit(celsius, fahrenheit_con_ruido)

# Obtener los coeficientes del modelo
coeficiente = model.coef_[0][0]
intercepto = model.intercept_[0]

print(f'Coeficiente (pendiente): {coeficiente}')
print(f'Intercepto: {intercepto}')

# Realizar predicciones
celsius_test = np.array([[-40], [0], [37], [100]])
fahrenheit_pred = model.predict(celsius_test)

# Calcular Fahrenheit exacto según la fórmula
fahrenheit_exacto = celsius_test * 9 / 5 + 32

# Mostrar resultados
resultados = pd.DataFrame({
    'Celsius': celsius_test.flatten(),
    'Farenheit (exacto)': fahrenheit_exacto.flatten(),
    'Fahrenheit Predicho': fahrenheit_pred.flatten()
})
print(resultados)

# Visualización
plt.scatter(celsius, fahrenheit, color='blue', label='Datos reales')
plt.plot(celsius, model.predict(celsius), color='red', label='Modelo de regresión')
plt.xlabel('Grados Celsius')
plt.ylabel('Grados Fahrenheit')
plt.legend()
plt.show()

# %%
