'''
Ejercicio 1: Desarrollar una función que Invierte el orden de los caracteres en una
cadena.
'''

def invertir_cadena(cadena):
    """
    Esta función invierte el orden de los caracteres en una cadena.

    Argumentos:
    cadena (str): La cadena que se desea invertir.

    Retorna:
    str: La cadena invertida.
    """
    return cadena[::-1]

# Programa principal
cadena_original = "Hola mundo"
cadena_invertida = invertir_cadena(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)