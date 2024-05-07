'''
ejercicio 3-4: especializar la funcion del punto 3.1 y 3.2 para que valide el numero
en un rango determinado pasado por parametro "desde" - "hasta"
'''

#Valida si el numero ingresado esta en el rango especificado
def validar_numero(numero, desde, hasta):
    if numero >= desde and numero <= hasta:
        print(True)
    else:
        print(False)

validar_numero(20, 10, 100)    