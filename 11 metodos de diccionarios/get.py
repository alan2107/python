'''
Si a un diccionario le falta una clave, al imprimir los valores
de las keys nos da error
'''
lista = [
{"edad":25,"nota":9},
{"nombre":"Jose","edad":34,"nota":8},
{"nombre":"Sol","edad":46,"nota":7},
{"nombre":"Beto","edad":28,"nota":6}
]

#con get le digo que sino encuentra nombre, que le agregue el string SIN NOMBRE
for e_nombre in lista:
    print(e_nombre.get("nombre", "SIN NOMBRE"))