def cuadrado(numero):
    return numero * numero

'''
En Python, la función map nos permite aplicar una función
sobre los items de un objeto iterable
'''

lista = [1,2,3,4,5]
resultado = map(cuadrado, lista)

lista_resultado = list(resultado)
print(lista_resultado)

#con lambda

lista = [1,2,3,4,5]
resultado = list(map(lambda numero:numero*numero, lista))

print(resultado)