""" Ejercicio 4: Una startup desea analizar las estadísticas de los usuarios de su sitio de
compras on-line recientemente lanzado al mercado para ello necesita un programa
que le permita acceder a los datos relevados. """

import listas_personas
from biblioteca import *

bandera = False


while True:
    menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        importar_listas()
        bandera = True
    elif opcion == "2":
        if bandera == True:
            listar_usuarios_mexico()
        else:
            print("Error.. Debe importar las listas")
    elif opcion == "3":
        if bandera == True:
            listar_datos_usuarios_brasil()
        else:
            print("Error.. Debe importar las listas") 
    elif opcion == "4":
        if bandera == True:
            listar_usuario_mas_joven()
        else:
            print("Error.. Debe importar las listas")
    elif opcion == "5":
        if bandera == True:
            promedio_edad_usuarios()
        else:
            print("Error.. Debe importar las listas")
    elif opcion == "6":
        if bandera == True:
            listar_usuario_mayor_edad_brasil()
        else:
            print("Error.. Debe importar las listas")
    elif opcion == "7":
        if bandera == True:
            listar_usuarios_mayor_8000()
        else:
            print("Error.. Debe importar las listas")
    elif opcion == "8":
        if bandera == True:
            listar_usuarios_italianos_mayores_40()
        else:
            print("Error.. Debe importar las listas")
    elif opcion == "9":
        if bandera == True:
            listar_datos_mexicanos_por_nombres(listas_personas.nombres, listas_personas.telefonos, listas_personas.mails, listas_personas.address, listas_personas.postalZip, listas_personas.region, listas_personas.country, listas_personas.edades)
        else:
            print("Error.. Debe importar las listas")
    elif opcion == "10":
        if bandera == True:
            listar_usuarios_mas_jovenes(listas_personas.nombres, listas_personas.telefonos, listas_personas.mails, listas_personas.address, listas_personas.postalZip, listas_personas.region, listas_personas.country, listas_personas.edades)
        else:
            print("Error.. Debe importar las listas")
    elif opcion == "11":
        if bandera == True:
            listar_usuarios_mexico_brasil_codigo_postal(listas_personas.nombres, listas_personas.telefonos, listas_personas.mails, listas_personas.address, listas_personas.postalZip, listas_personas.region, listas_personas.country, listas_personas.edades)
        else:
            print("Error.. Debe importar las listas")
    elif opcion == "12":
        break
    else:
        print("Opción no válida. Intente nuevamente.")