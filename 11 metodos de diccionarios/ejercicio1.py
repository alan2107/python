'''
DICCIONARIOS
Ejercicio 1: Se trabajará con el archivo estudiantes.py
Realizar una función con el siguiente Menú de Opciones:

1-Listar los alumnos por orden ascendente de apellido, si se repite,
ordenar por nombre. Mostrar legajo, nombre, apellido y edad
2-Obtener el promedio de notas para cada estudiante
3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el
programa de “Ingenieria en Informatica”
4-Obtener un promedio de edad de los estudiantes. Mostrar nombre y
apellido
5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y
apellido
6-Listar nombre y apellido de los alumnos que forman el grupo “Club de
Informática” con sus respectivos promedios
7-Listar legajo, nombre, apellido y programas que cursan los alumnos
más jóvenes.

Ejercicio 2: Crear una función para cada opción de menú.
Ejercicio 3: Desarrollar las funciones en una biblioteca.
'''
from estudiantes import *
from  stark.biblioteca import * 

alumnos = estudiantes


while True:
    menu()
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        listar_alumnos_ordenados(alumnos)
    elif opcion == 2:
        obtener_promedio_notas(alumnos)
    elif opcion == 3:
        listar_estudiantes_ingenieria(alumnos)
    elif opcion == 4:
        obtener_promedio_edad(alumnos)
    elif opcion == 5:
        alumno_mayor_promedio(alumnos)
    elif opcion == 6:
        listar_alumnos_club_informatica(alumnos)
    elif opcion == 7:
        listar_alumnos_mas_jovenes(alumnos)
    elif opcion == 0:
        break
    else:
        print("Opción no válida, intente nuevamente.")