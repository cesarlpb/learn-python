# Propuesta de solución del ejercicio 2

import pandas as pd
import matplotlib.pyplot as plt

def main():
  # Cargar el dataset
  data = pd.read_csv('data.csv')

  # Histograma de alturas
  plt.figure(figsize=(10, 6))
  plt.hist(data['height'], bins=30, edgecolor='black')
  plt.title('Histograma de Alturas')
  plt.xlabel('Altura (cm)')
  plt.ylabel('Frecuencia')
  plt.show()

  # Diagrama de dispersión de pesos vs edades
  plt.figure(figsize=(10, 6))
  plt.scatter(data['age'], data['weight'], alpha=0.5)
  plt.title('Diagrama de Dispersión de Pesos vs Edades')
  plt.xlabel('Edad')
  plt.ylabel('Peso (kg)')
  plt.show()

  # Gráfica de barras de promedios de altura por género
  height_means = data.groupby('gender')['height'].mean()

  plt.figure(figsize=(10, 6))
  height_means.plot(kind='bar', color=['blue', 'orange'])
  plt.title('Promedio de Altura por Género')
  plt.xlabel('Género')
  plt.ylabel('Altura Promedio (cm)')
  plt.xticks(rotation=0)
  plt.show()

if __name__ == '__main__':
  main()