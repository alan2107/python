def es_par(n):
    return n % 2 == 0

lista = [1,2,3,4,5]

lista_pares = list(filter(es_par, lista))

print(lista_pares )

#con lambda

lista = [1,2,3,4,5]

lista_pares = list(filter(lambda n: True if n % 2 == 0 else False, lista))
print(lista_pares)