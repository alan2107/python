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

def menu():
    while True:
        print("Menú de Opciones:")
        print("1- Listar los alumnos por orden ascendente de apellido")
        print("2- Obtener el promedio de notas para cada estudiante")
        print("3- Listar estudiantes de Ingenieria en Informatica")
        print("4- Obtener un promedio de edad de los estudiantes")
        print("5- Informar el alumno con mayor promedio de notas")
        print("6- Listar alumnos del Club de Informatica con sus promedios")
        print("7- Listar alumnos más jóvenes")
        print("0- Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 0:
            break
        else:
            print("Opción no válida, intente nuevamente.")