# Propuesta de solución del ejercicio 3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generar datos de ejemplo
celsius = np.array(range(-40, 101, 10))  # Desde -40 hasta 100 grados Celsius
COEFICIENTE_RUIDO = 5
fahrenheit = celsius * 9/5 + 32 + COEFICIENTE_RUIDO * np.random.randint(-2, 3, size=celsius.shape)  # Conversión a Fahrenheit con error
# Nota: si colocais el coeficiente de ruido a cero no habrá error y el ajuste será perfecto con r^2 == 1

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(celsius.reshape(-1, 1), fahrenheit, test_size=0.2, random_state=0)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular el error cuadrático medio y el coeficiente de determinación (R^2)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Error Cuadrático Medio            : {mse}")
print(f"Coeficiente de Determinación (R^2): {r2}")

# Ecuación del modelo
intercept = model.intercept_
coef = model.coef_[0]
print(f"Ecuación del modelo: Fahrenheit = {coef:.2f} * Celsius + {intercept:.2f}")

if COEFICIENTE_RUIDO:
  print("Conclusión: Si hay ruido (equivale a que los datos no sean exactos), no coincide con la ecuación exacta: F = 9/5 * C + 32")
else:
  print("Conclusión: Coincide con la ecuación exacta: F = 1.8 * C + 32")


# Graficar las predicciones vs los valores reales
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Valores reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicciones')
plt.title('Predicciones vs Valores Reales')
plt.xlabel('Temperatura en Celsius')
plt.ylabel('Temperatura en Fahrenheit')
plt.legend()
plt.show()
