""" Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango
especificado, validar los números solicitados dentro de ese rango, guardar en una
lista y retornarla. El programa principal debe invocar a la función y mostrar por
pantalla el retorno. """

def pedir_numeros_en_rango(minimo, maximo, cantidad):
    numeros = []
    for i in range(cantidad):
        num = int(input(f"Ingrese el número {i+1} (entre {minimo} y {maximo}): "))
        while num < minimo or num > maximo:
            num = int(input(f"El número debe estar dentro del rango. Ingrese otro número (entre {minimo} y {maximo}): "))
        numeros.append(num)
    return numeros

# Programa principal
minimo = int(input("Ingrese el límite inferior del rango: "))
maximo = int(input("Ingrese el límite superior del rango: "))
cantidad_numeros = 10

numeros_ingresados = pedir_numeros_en_rango(minimo, maximo, cantidad_numeros)

print("Los números ingresados dentro del rango son:")
print(numeros_ingresados)