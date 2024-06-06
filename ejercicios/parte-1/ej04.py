# https://pythondiario.com/2013/05/ejercicios-en-python-parte-1.html
"""
4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""
#%% Verificar si el elemento está en una lista:
frutas = ["manzana", "pera", "kiwi"]
fruta_random = "kiwi"
print(fruta_random in frutas)
#%% Ejercicio:
# vocales_lista = [...]
def verificar_vocal(vocal: str) -> bool:
  pass
#%% Test
assert verificar_vocal('a') == True
assert verificar_vocal('z') == False
