'''
Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida
posición y número a guardar al usuario, lo guarde en una lista en la posición
solicitada aleatoriamente y la retorne. El programa principal debe invocar a la
función y mostrar por pantalla el retorno.
'''
def inicializar_lista():
    return [0] * 10

def cargar_lista_en_posicion(lista):
    posicion = int(input("Ingresa la posicion donde quieres guardar el numero (0-9): "))
    if posicion < 0 or posicion > 9:
        print("La posicion debe estar entre 0 y 9.")
    else:
        numero = int(input("Ingresa el numero que quieres guardar: "))
        lista[posicion] = numero
    return lista

lista_de_numeros = inicializar_lista()
print("Lista inicializada:", lista_de_numeros)
lista_con_numero = cargar_lista_en_posicion(lista_de_numeros)
cargar_lista_en_posicion(lista_de_numeros)