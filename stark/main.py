from data_stark import lista_personajes
from biblioteca import *
'''
Realizar una función con el siguiente Menú de Opciones:
A. Listar ordenado por Nombre. Lista todos los datos de cada superhéroe ordenados por
Nombre de manera ascendente.
B. Listar Masculinos débiles. Recorrer la lista y determinar cuál es el superhéroe más débil de
género M.
C. Cantidad por color de ojos. Determinar cuántos superhéroes tienen cada tipo de color de
ojos.
D. Listar por color de Pelo. Listar todos los superhéroes agrupados por color de pelo.
E. Listar inteligencia. Listar todos los superhéroes agrupados por tipo de inteligencia.
F. Listar Promedio. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género
femenino
G. Asignar IMC. Calcular el índice de masa corporal de cada superhéroe y guardarla en un
nuevo campo. Se deberá hacer uso de una función lambda que asignará a cada superhéroe el
IMC calculado.

Nota:
Crear una función para cada opción de menú.
Desarrollar las funciones en una biblioteca.
Utilizar todo lo visto en clases, métodos, funciones lambda, operadores ternarios, etc.
'''
personajes = lista_personajes

while True:
    menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == 'A':
        resultado = ordenar_por_nombre(personajes)
        for personaje in resultado:
            print(personaje)
    elif opcion == 'B':
        resultado = listar_masculinos_debiles(personajes)
        print(resultado)
    elif opcion == 'C':
        resultado = calcular_cantidad_color_de_ojos(personajes)
        print(resultado)
    elif opcion == 'D':
        resultado = listar_por_color_pelo(personajes)
        for color, personajes in resultado.items():
            print(f"{color}: {personajes}")
    elif opcion == 'E':
        resultado = listar_inteligencia(personajes)
        for inteligencia, personajes in resultado.items():
            print(f"{inteligencia}: {personajes}")
    elif opcion == 'F':
        resultado = listar_promedio(personajes)
        for nombre, peso in resultado:
            print(f"Nombre: {nombre}, Peso: {peso}")
    elif opcion == 'G':
        resultado = agregar_imc(personajes)
        for personaje in resultado:
            print(personaje)
    elif opcion == 'H':
        break
    else:
        print("Opción no válida, intente nuevamente.")