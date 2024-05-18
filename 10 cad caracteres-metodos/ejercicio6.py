'''
Ejercicio 6: Desarrollar una función que verifique si una cadena es un palíndromo:
Palíndromo: Palabra o frase cuyas letras están dispuestas de tal manera que resulta
la misma leída de izquierda a derecha que de derecha a izquierda; por ejemplo,
anilina.
'''

def es_palindromo(cadena):
    """
    Esta función verifica si una cadena es un palíndromo.

    Argumentos:
    cadena (str): La cadena que se desea verificar.

    Retorna:
    bool: True si la cadena es un palíndromo, False en caso contrario.
    """
    # Convertimos la cadena a minúsculas y eliminamos los espacios en blanco
    cadena = cadena.lower().replace(" ", "")
    # Verificamos si la cadena es igual a su reverso
    return cadena == cadena[::-1]

# Ejemplo de uso:
cadena = "anilina"
if es_palindromo(cadena):
    print(f'"{cadena}" es un palíndromo.')
else:
    print(f'"{cadena}" no es un palíndromo.')