'''
Ejercicio 7: Desarrollar una función “ordenar” que recibe un string y un número (1 o
-1). Se debe retornar el string ordenado de manera ascendente (si recibió 1 por
parámetros) o descendente (si recibió -1)
Nota: Determinar parámetros y retornos de manera que las funciones sean
genéricas y reutilizables.
'''

def ordenar(cadena, orden=1):
    """
    Esta función ordena una cadena de manera ascendente o descendente.

    Argumentos:
    cadena (str): La cadena que se desea ordenar.
    orden (int): El orden de clasificación, 1 para ascendente y -1 para descendente.
                 Por defecto, es 1 (ascendente).

    Retorna:
    str: La cadena ordenada.
    """
    # Convertimos la cadena en una lista de caracteres
    caracteres = list(cadena)
    # Ordenamos la lista de caracteres según el parámetro 'orden'
    caracteres.sort(reverse=(orden == -1))
    # Unimos los caracteres ordenados en una cadena
    cadena_ordenada = ''.join(caracteres)
    return cadena_ordenada

# Ejemplo de uso:
cadena = "zyxwvutsrqponmlkjihgfedcba"
orden_ascendente = ordenar(cadena)
orden_descendente = ordenar(cadena, orden=-1)

print("Cadena original:", cadena)
print("Cadena ordenada ascendente:", orden_ascendente)
print("Cadena ordenada descendente:", orden_descendente)