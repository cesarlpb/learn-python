# Propuesta de solución del ejercicio 1

# Importaciones
import time
import sys
import numpy as np

def main():
  # Definición de constantes y variables para el programa
  num_elements = 1_000_000
  list_data = list(range(num_elements))
  array_data = np.arange(num_elements)

  # Conseguimos los tamaños en memoria
  list_memory = sys.getsizeof(list_data)    # bytes
  array_memory = sys.getsizeof(array_data)  # bytes

  print("MEMORIA")
  print(f"Uso de memoria de la lista  : {list_memory} bytes")
  print(f"Uso de memoria del np.array : {array_memory} bytes")
  print(f"Diferencia                  : {abs(list_memory - array_memory)} bytes")
  print(f"Diferencia %                : {abs(list_memory - array_memory) / ((list_memory + array_memory) / 2) * 100} %")
  print(f"Conclusión                  : la diferencia es muy pequeña en memoria con muchos datos")
  print("")

  # Suma de elementos en la lista
  start_time = time.time()    # hora de inicio
  list_sum = sum(list_data)   # ejecutamos el algoritmo
  end_time = time.time()      # hora de finalización
  list_sum_time = end_time - start_time # diferencia := tiempo que ha tardado el algoritmo

  # Suma de elementos en el np.array
  start_time = time.time()
  array_sum = np.sum(array_data)
  end_time = time.time()
  array_sum_time = end_time - start_time

  print("TIEMPO")
  print(f"Tiempo de suma en la lista    : {list_sum_time} segundos")
  print(f"Tiempo de suma en el np.array : {array_sum_time} segundos")
  print(f"Diferencia                    : {abs(list_sum_time - array_sum_time)} segundos")
  print(f"Diferencia %                  : {abs(list_sum_time - array_sum_time) / ((list_sum_time + array_sum_time) / 2) * 100} %")
  print(f"Conclusión                    : la diferencia es notable, el método con Numpy es mucho más rápido")
  print("")

  constant = 1_000 # constante a multiplicar por toda la lista o np.array

  # Multiplicación de elementos en la lista
  start_time = time.time()
  list_mult = [x * constant for x in list_data] # bucle con list comprehension
  end_time = time.time()
  list_mult_time = end_time - start_time

  # Multiplicación de elementos en el np.array
  start_time = time.time()
  array_mult = array_data * constant
  end_time = time.time()
  array_mult_time = end_time - start_time

  print("MULTIPLICACION")
  print(f"Tiempo de multiplicación en la lista    : {list_mult_time} segundos")
  print(f"Tiempo de multiplicación en el np.array : {array_mult_time} segundos")
  print(f"Diferencia                              : {abs(list_mult_time - array_mult_time)} segundos")
  print(f"Diferencia %                            : {abs(list_mult_time - array_mult_time) / ((list_mult_time + array_mult_time) / 2) * 100} %")
  print(f"Conclusión                              : la diferencia es notable, el método con Numpy es mucho más rápido")
  print("")
  

if __name__ == '__main__':
  main()