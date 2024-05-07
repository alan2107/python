'''
Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor
solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a
dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado
por pantalla. Atención: pueden reutilizarse funciones ya creadas.
'''

#Funciones

#recibe como parametro un numero
def recibe_numero(numero):
    numero = float(input("Ingrese numero: "))
    return numero

#recibe un numero como parametro y validad si entra en rango
def validar_numero(numero):
    if numero >= 10 and numero <= 100:
        print("El numero ingresado esta adentro del rango")
    else:
        print("Error.. el numero ingresado no entro en el rango")

def realizar_descuento(numero):
    descuento = numero * 0.05
    numero_con_descuento = numero - descuento
    return numero_con_descuento

#Empieza mi programa

numero1 = None
numero_ingresado = recibe_numero(numero1)
print("Su numero es: ", numero_ingresado)
validar_numero(numero_ingresado)
numero_con_descuento = realizar_descuento(numero_ingresado)

print("Su numero con descuento es: ", numero_con_descuento)