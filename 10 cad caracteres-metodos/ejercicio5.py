'''
Ejercicio 5: Desarrollar una función que capitalice palabras en una cadena.
'''

def capitalizar_palabras(cadena):
    """
    Esta función capitaliza todas las palabras en una cadena.

    Argumentos:
    cadena (str): La cadena en la que se capitalizarán las palabras.

    Retorna:
    str: La cadena con todas las palabras capitalizadas.
    """
    palabras = cadena.split()  # Dividimos la cadena en palabras
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]  # Capitalizamos cada palabra
    return ' '.join(palabras_capitalizadas)  # Unimos las palabras capitalizadas en una cadena

# Ejemplo de uso:
cadena_original = "hola mundo! este es un ejemplo de capitalización de palabras."
cadena_capitalizada = capitalizar_palabras(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena capitalizada:", cadena_capitalizada)