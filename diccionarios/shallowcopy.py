from copy import deepcopy

""" lista = [1,2,3,4,5]

print(lista)

copia_lista = lista.copy()
print(copia_lista)
copia_lista[2] = 30

print(copia_lista)
print(lista) """

#shallow copy no me sirve cuando los elementos son compuestos. sirven para uno simple

""" lista2 = [{"nombre": "Ana", "edad": 25, "nota":9},
        {"nombre": "Jose", "edad": 34, "nota":8},
        {"nombre": "Sol", "edad": 46, "nota":7},
        {"nombre": "Beto", "edad": 28, "nota":6}]

copia_lista2 = lista2.copy()
print(copia_lista2)
copia_lista[2]["nombre"] = "Roberto"

print(copia_lista2)
print(lista2) """

#en este caso se usa el deep copy que es para trabajar con elementos compuestos
lista_alumnos = [{"nombre": "Ana", "edad": 25, "nota":9},
        {"nombre": "Jose", "edad": 34, "nota":8},
        {"nombre": "Sol", "edad": 46, "nota":7},
        {"nombre": "Beto", "edad": 28, "nota":6}]

copia_lista = deepcopy(lista_alumnos)
copia_lista[3]["nombre"] = "Roberto"

print(copia_lista)
print(lista_alumnos)