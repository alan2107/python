'''
Ejercicio 3-7: Realizar un programa que: asigne a las variables numero1 y numero2
los valores solicitados al usuario, valide los mismos entre 10 y 100, asigne a la
variable operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice
la operación de dichos valores a través de una función. Mostrar el resultado por pantalla
'''
# FUNCIONES

def restar(numero1, numero2):
    return numero1 - numero2

def sumar(numero1, numero2):
    return numero1 + numero2

def validar(valor):
    return 10 >= valor <= 100

def validar_operacion(operacion):
    return operacion.lower() in ["s" ,"r"]

def obtener_valor(mensaje):
    valor = None
    while valor is None:
        entrada = input(mensaje)
        if entrada.isdigit():
            valor = int(entrada)
            if not validar(valor):
                print("El valor debe estar entre 10 y 100.")
                valor = None
        else:
            print("Por favor, ingrese un numero valido")
    return valor

#Programa

numero1 = obtener_valor("Ingrese el primero numero(entre de 10 a 100): ")
numero2 = obtener_valor("Ingrese el segundo numero(entre de 10 a 100): ")

operacion = input("Ingrese la operacion a realizar ('s' para sumar, 'r' para restar): ")
while not validar_operacion(operacion):
    operacion = input("Error.. Porfavor, Ingrese 's' para sumar. 'r' para restar: ")

if operacion.lower() == 's':
    resultado = sumar(numero1, numero2)
    print("El resultado de la suma es: ", resultado)

else:
    resultado = restar(numero1, numero2)
    print("El resultado de la suma es: ", resultado) 