'''
sort() solo funciona con listas y ordena la propia lista
seleccionada. No posee un valor de retorno.
'''

mi_lista = [67, 2, 999, 1, 15]
mi_lista.sort()
print("Lista Ordenada: ", mi_lista) #Lista Ordenada: [1, 2, 15, 67, 999]

mi_lista.sort(reverse=True)
print("Lista Ordenada descendente: ", mi_lista) #Lista Ordenada descendente: [999, 67, 15, 2, 1]

#con lambda

lista = [{"nombre": "Ana","edad": 25, "nota":9},
         {"nombre": "Jose","edad": 34, "nota":8},
         {"nombre": "Sol","edad": 46, "nota":7},
         {"nombre": "Beto","edad": 28, "nota":6}]

#ordenar por nota

lista.sort(key=lambda alumno : alumno["nota"], reverse=True)
print(lista)


#sorted

nombres = [ "Pedro", "Ana", "Soledad", "Juan", "Roberto"]
nombres_ordenados = sorted(nombres, reverse=True)
print("Ordenados descendente: ",nombres_ordenados)