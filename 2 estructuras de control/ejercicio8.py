'''
Ejercicio 8:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
mostrar el número repetido
'''
lista = [82, 3, 49, 38, 94, 85, 95, 92, 6, 58, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] == lista[j]:
            print("El numero repetido de la lista es: ", lista[i])
            break