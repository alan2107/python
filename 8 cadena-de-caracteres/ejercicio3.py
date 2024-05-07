'''
Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número.
Se debe retornar el caracter en la posición indicada por el número si ésta es válida.
**IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el
<número de caracteres> - 1.
'''

def char_at(cadena, numero):
    if numero < 0 or numero >= len(cadena):
        print("La posicion no es valida")
    else:
        return cadena[numero]

cadena = "hola profe"
numero = 3
caracter = char_at(cadena,numero)
print(f"El caracter en la posicion {numero} es: '{caracter}'")