""" Ejercicio 2: Dadas las siguientes listas:
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias
Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
"Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
Desarrollar una función que realice el ordenamiento de las listas por nombre de
manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera
descendente. """

nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos","Base de Datos", "Ergonomia", "Naturaleza"]
puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

def ordenar_por_nombre_y_puntos(nombres, puntos):
    
    # Algoritmo de ordenamiento burbuja
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            # Ordenar por nombre de manera ascendente
            if nombres[i] > nombres[j]:
                    # Intercambiar nombres y puntos
                    aux_nombre = nombres[i]
                    aux_puntos = puntos[i]
                    nombres[i] = nombres[j]
                    puntos[i] = puntos[j]
                    nombres[j] = aux_nombre
                    puntos[j] = aux_puntos
            # Si los nombres son iguales, ordenar por puntos de manera descendente
            elif puntos[i] < puntos[j]:
                # Intercambiar puntos
                aux_puntos = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = aux_puntos

    return nombres, puntos

ordenar_por_nombre_y_puntos(nombres, puntos)

print(nombres, puntos)