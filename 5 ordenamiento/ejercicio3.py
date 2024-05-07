""" Ejercicio 3: Dadas las siguientes listas:
Estudiantes =
["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Anto
nio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos =
[“Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui"
,"Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
Desarrollar una función que realice el ordenamiento de las listas por apellido de
manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera
ascendente, si el nombre también es el mismo, debe ordenar por nota de manera
descendente. """

estudiantes =["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
apellidos =["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def ordenar_por_apellido_nombre_y_nota(apellidos:list, estudiantes:list, notas: list)->list:
    for i in range(len(apellidos)-1):
            for j in range(i + 1, len(apellidos)):
                if apellidos[i] > apellidos[j]:
                    # Intercambiar estudiantes, apellidos y notas
                    aux_estudiante = estudiantes[i]
                    aux_apellido = apellidos[i]
                    aux_nota = notas[i]
                    estudiantes[i] = estudiantes[j]
                    apellidos[i] = apellidos[j]
                    notas[i] = notas[j]
                    estudiantes[j] = aux_estudiante
                    apellidos[j] = aux_apellido
                    notas[j] = aux_nota
                # Si los apellidos son iguales, ordenar por nombre de manera ascendente
                elif estudiantes[i] != estudiantes[j]:
                    if estudiantes[i] > estudiantes[j]:
                        # Intercambiar estudiantes y notas
                        aux_estudiante = estudiantes[i]
                        aux_nota = notas[i]
                        estudiantes[i] = estudiantes[j]
                        notas[i] = notas[j]
                        estudiantes[j] = aux_estudiante
                        notas[j] = aux_nota
                # Si los apellidos y nombres son iguales, ordenar por nota de manera descendente
                elif notas[i] < notas[j]:
                    # Intercambiar notas
                    aux_nota = notas[i]
                    notas[i] = notas[j]
                    notas[j] = aux_nota
    return apellidos, estudiantes, notas

ordenar_por_apellido_nombre_y_nota(estudiantes, apellidos, nota)
print(estudiantes, apellidos, nota)