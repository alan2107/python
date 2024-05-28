lista = [
{"edad":25,"nota":9},
{"nombre":"Jose","edad":34,"nota":8},
{"nombre":"Sol","edad":46,"nota":7},
{"nombre":"Beto","edad":28,"nota":6}
]


valor_eliminado = lista[1].pop("nombre","NO EXISTE") #el segundo parametro le paso que me avise que no existe
#Valor eliminado = NO EXISTE

print(lista)