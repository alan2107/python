#parsear un JSON
import json

def parse_json(archivo:str)-> list:
    with open(archivo, "r") as archivo:
        tema = json.load(archivo)
    return tema["bzrp"] 

try:
    lista = parse_json("data.json")
    print(lista[0])
except FileNotFoundError:
    print("El archivo no existe")
except IndexError:
    print("Error de indice")