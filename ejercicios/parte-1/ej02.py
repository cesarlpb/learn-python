# https://pythondiario.com/2013/05/ejercicios-en-python-parte-1.html
"""
  2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""

# %% Extensión de la función calcular_maximo_dos del ej01:
def calcular_maximo_tres(a, b, c):
  pass # escribe aquí la solución

# %% Tests
r_1 = calcular_maximo_tres(1, 2, 3) # 3
assert r_1 == 3

# %% ¿Cómo se puede calcular el máximo o mínimo de una lista de números?
# Por simplicidad podemos suponer que son int
def calcular_maximo_lista(lista: list):
  pass # escribe aquí la solución
# %% Tests
lista = [-1, 0, 1] # max -> 1
res = calcular_maximo_lista(lista)
assert res == 1