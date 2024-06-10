# https://pythondiario.com/2013/05/ejercicios-en-python-parte-1.html
"""
  2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""

# %% Extensión de la función calcular_maximo_dos del ej01:
def calcular_maximo_tres(a, b, c):
  # compruebas si a es mayor:
  if a > b and a > c:
    return a
  # compruebas si b es mayor:
  elif b > a and b > c:
    return b
  # si ninguno es mayor, devuelvo c:
  else:
    return c

# %% Tests
r_1 = calcular_maximo_tres(1, 2, 3)    # 3
r_2 = calcular_maximo_tres(5, -1, 5)   # 5
r_3 = calcular_maximo_tres(10, 10, 10) # 10

assert r_1 == 3
assert r_2 == 5
assert r_3 == 10

# %% ¿Cómo se puede calcular el máximo o mínimo de una lista de números?
# Por simplicidad podemos suponer que son int
def calcular_maximo_lista(lista: list) -> int | None:
  maximo_actual = None
  # Si no hay elementos, retornamos None:
  if not len(lista):
    return None
  # hay que tener elementos en la lista:
  else:
    for i, num in enumerate(lista):
      if i == 0:
        maximo_actual = num # primer elemento
      else:
        if num > maximo_actual:
          maximo_actual = num
  return maximo_actual
    

# %% Tests
lista = [-1, 0, 1] # max -> 1
res = calcular_maximo_lista(lista)
assert res == 1

lista = [7, 7, 7] # 7
res = calcular_maximo_lista(lista)
assert res == 7

lista = [] # No hay máximo -> None
res = calcular_maximo_lista(lista)
assert res is None

lista = [1] # 1
res = calcular_maximo_lista(lista)
assert res == 1

#%%  