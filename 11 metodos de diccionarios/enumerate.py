lista = ["Lavar las papas",
"Colocar en una cacerola con agua",
"Cocinar por media hora",
"Servir frio"]

'''
Podemos usar la función enumerate() con un bucle for para
imprimir los valores de un iterable junto a un contador.
'''

for i, lista in enumerate(lista, start=1):
    print(i ,lista)