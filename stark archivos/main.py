from bibliotecaArchivos import *
import json
import csv

lista_heroes = []
while True:
    menu()
    opcion = input("Seleccione una opcion: ")

    if opcion == 'A':
        lista_heroes = opcion_leer_json()
    elif opcion == 'B':
        lista_heroes = opcion_ordenar_heroes(lista_heroes)
    elif opcion == 'C':
        opcion_guardar_csv(lista_heroes)
    elif opcion == 'D':
        print("Saliendo del programa.")
        break
    else:
        print("opcion no valida, intente nuevamente.")
