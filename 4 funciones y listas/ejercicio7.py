""" Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de
compras on-line recientemente lanzado al mercado para ello necesita un programa
que le permita acceder a los datos relevados.

Realizar una función con el siguiente Menú de Opciones:

1-Importar listas
2-Listar los datos de los usuarios de México
3-Listar los nombre, mail y teléfono de los usuarios de Brasil
4-Listar los datos del/los usuario/s más joven/es
5-Obtener un promedio de edad de los usuarios
6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
7-Listar los datos de los usuarios de México y Brasil cuyo código postal
sea mayor a 8000
8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40
años.

Ejercicio 8: Crear una función para cada opción de menú.
Ejercicio 9: Desarrollar las funciones en una biblioteca.
Nota: No se podrá acceder a ninguna opción de menú si no se realizó la importación
de las listas. """

# Definir las listas de datos de usuarios
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
        break
    else:
        print("Opción no válida. Intente nuevamente.")
