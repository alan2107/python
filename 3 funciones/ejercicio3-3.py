'''
ejercicio 3-3: Crear una funcion que permita determinar si un numero es para o no.
la funcion retorna "True en caso afirmativo y "False" en caso contrario. probar en el 
programa principal realizado la invocacion llamada. 
'''

def determinar_si_es_par(numero):
    if numero %2 == 0:
        print(True)
    else:
        print(False)

determinar_si_es_par(180)