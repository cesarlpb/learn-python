# https://pythondiario.com/2013/05/ejercicios-en-python-parte-1.html
"""
3 - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""
# %% built-in len:
string = "Hola"
print(len(string))

# %% bucle
def contar_chars(string: str) -> int:
  pass # -> return
#%% Tests
string = "Hola, qué tal?" # 14
assert contar_chars(string) == 14