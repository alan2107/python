""" Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números
y un número especificado. La misma debe buscar el número especificado en la lista
y retornar “True” si existe. """

def buscar_numero(lista, numero):
    return numero in lista

# Ejemplo de uso de la función
numeros = [1, 3, 5, 7, 9]
numero_especificado = 5

if buscar_numero(numeros, numero_especificado):
    print(f"El número {numero_especificado} está en la lista.")
else:
    print(f"El número {numero_especificado} no está en la lista.")