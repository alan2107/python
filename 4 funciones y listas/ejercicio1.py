'''
Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los
guarde en una lista y la retorne. El programa principal debe invocar a la función y
mostrar por pantalla el retorno.
'''
    #Funcion
def pedir_nombres(lista:list)->list:
    nombres = []
    for i in range(10):
        nombre= input("Ingrese un nombre: ")
        nombres.append(nombre)

    return print("su lista de nombres es: ", nombres)

#Programa principal
lista = []
pedir_nombres(lista)