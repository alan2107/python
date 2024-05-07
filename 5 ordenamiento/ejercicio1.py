""" Ejercicio 1: Dadas las siguientes listas:
Nombres =
["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Anto
nio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que realice el ordenamiento de las listas por nombre de
manera ascendente. """
def ordenar_nombres(nombres, edades):

    for i in range(len(nombres)-1):
        for j in range(i+1, len(nombres)):
            if nombres[i] > nombres[j]:
                #intercambiar nombres
                aux_nombre = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux_nombre
                #Intercambiar edades para mantener la correspondencia
                aux_edad = edades[i]
                edades[i] = edades[j]
                edades[j] = aux_edad
    return nombres, edades

nombres =["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

ordenar_nombres(nombres , edades)

print(nombres, edades)