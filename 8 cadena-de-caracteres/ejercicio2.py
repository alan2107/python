'''
Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices.
Se debe retornar la cadena que va entre las posiciones indicadas por los índices.
Si las posiciones no son válidas se debe informar.
'''

def cadena_entre_indices(cadena, a, b):
    if a < 0 or b >= len(cadena) or a >= b:
        print("Las posiciones no son validas")
    else:
        return cadena[a:b+1]
    
# Ejemplo de uso:
cadena = "la profe me da doble estrellita"
a = 15
b = 30
resultado = cadena_entre_indices(cadena, a, b)
print(f"La cadena entre los índices {a} y {a} es: '{resultado}'")