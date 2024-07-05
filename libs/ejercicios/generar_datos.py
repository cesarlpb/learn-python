# Script que genera datos para el ejercicio 2

import pandas as pd
import numpy as np

# Generar datos de muestra
np.random.seed(0)

num_samples = 1000
ages = np.random.randint(18, 80, num_samples)
heights = np.random.normal(170, 10, num_samples)  # media 170 cm, desviación estándar 10 cm
weights = np.random.normal(70, 15, num_samples)  # media 70 kg, desviación estándar 15 kg
genders = np.random.choice(['Male', 'Female'], num_samples)

# Crear un DataFrame
data = pd.DataFrame({
    'age': ages,
    'height': heights,
    'weight': weights,
    'gender': genders
})

# Guardar a un archivo CSV
data.to_csv('./data.csv', index=False)
print("Se ha creado el CSV")