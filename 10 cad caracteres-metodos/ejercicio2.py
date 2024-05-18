'''
Ejercicio 2: Desarrollar una función que cuente cuántas palabras hay en una cadena.
'''

def contar_palabras(cadena):
    """
    Esta función cuenta cuántas palabras hay en una cadena.

    Argumentos:
    cadena (str): La cadena en la que se contarán las palabras.

    Retorna:
    int: El número de palabras en la cadena.
    """
    # Eliminamos los espacios en blanco al principio y al final de la cadena
    cadena = cadena.strip()
    # Dividimos la cadena en palabras utilizando los espacios como separadores
    palabras = cadena.split()
    # Contamos cuántas palabras hay en la lista resultante
    return len(palabras)

# Ejemplo de uso:
cadena = "Esta es una cadena de ejemplo"
num_palabras = contar_palabras(cadena)
print("Número de palabras en la cadena:", num_palabras)