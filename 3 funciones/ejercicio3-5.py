'''
Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la
funcion restar en sus combinaciones.
Restar1(int, int)->int:
Restar2()->int:
Restar3(int, int):
Restar4():
'''

# resta 2 numeros y vuelve resultado
def restar1(int1, int2)-> int:
    return int1 - int2

#solicita al usuario 2 numeros y vuelve la resta del mismo
def restar2()->int:
    int1 = int(input("Ingrese numero a restar: "))
    int2 = int(input("Ingrese segundo numero a restar: "))

    return int1 - int2

#resta 2 numeros y muestra el resultado
def restar3(int1, int2):
    resultado = int1 - int2

    print("El resultado de la resta entre", int1, "y", int2, "es", resultado)

#solicita 2 numeros y muestra la resta del mismo
def restar4():
    int1 = int(input("Ingrese numero a restar: "))
    int2 = int(input("Ingrese segundo numero a restar: "))

    resultado = int1 - int2
    print("El resultado de la resta entre", int1, "y", int2, "es", resultado)