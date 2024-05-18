'''
Ejercicio 3: Desarrollar una función que reemplaza una palabra específica por otra
en una cadena.
'''

def reemplazar_palabra(cadena, palabra_a_reemplazar, nueva_palabra):
    """
    Esta función reemplaza una palabra específica por otra en una cadena.

    Argumentos:
    cadena (str): La cadena en la que se realizará el reemplazo.
    palabra_a_reemplazar (str): La palabra que se desea reemplazar.
    nueva_palabra (str): La palabra con la que se desea reemplazar.

    Retorna:
    str: La cadena con la palabra reemplazada.
    """
    # Usamos el método replace para realizar el reemplazo
    nueva_cadena = cadena.replace(palabra_a_reemplazar, nueva_palabra)
    return nueva_cadena

# Ejemplo de uso:
cadena_original = "Esta es una cadena de ejemplo"
palabra_a_reemplazar = "cadena"
nueva_palabra = "frase"
cadena_reemplazada = reemplazar_palabra(cadena_original, palabra_a_reemplazar, nueva_palabra)
print("Cadena original:", cadena_original)
print("Cadena con la palabra reemplazada:", cadena_reemplazada)