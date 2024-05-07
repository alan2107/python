lista = [34, 23, 45, 89, 1234, 82, 99]

#ORDENA DE MANERA ASCENDENTE
for i in range(len(lista)-1):
    for j in range(i + 1, len(lista)):
        if (lista[i] > lista[j]):
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(lista)

#ORDENA DE MANERA DESCENDENTE
for i in range(len(lista)-1):
    for j in range(i + 1, len(lista)):
        if (lista[i] < lista[j]):
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(lista)