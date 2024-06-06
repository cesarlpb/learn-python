# https://pythondiario.com/2013/05/ejercicios-en-python-parte-1.html

"""
  1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

# %% Esto es una celda
print("Hola")

# %% Esto es otra celda
print(1+1)
print("2")

# %% Empezamos a resolver el ejercicio aquí:

# Vamos a considerar que a y b son int
def calcular_maximo_dos(a: int, b: int) -> int:
    """
    Calcula el valor máximo entre dos números enteros.

    Parameters:
    a (int): El primer número entero.
    b (int): El segundo número entero.

    Returns:
    int: El mayor de los dos números enteros proporcionados.
    """
    if a > b:
        return a
    else:
        return b



# %%
r_1 = calcular_maximo_dos(1, 3) # 3
r_2 = calcular_maximo_dos('1', '2') # '2'
r_3 = calcular_maximo_dos(5, 5) # 5

assert r_1 == 3
assert r_2 == '2' # no es int
assert r_3 == 5


# %%
