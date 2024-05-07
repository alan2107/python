""" Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo
listas_personas.py. Importar los nombres a una lista. Realizar una función que
muestre los mismos. """

from listas_personas import nombres  

# Definir una función para mostrar los nombres
def mostrar_nombres():
    print("Lista de nombres:")
    for nombre in nombres:
        print(nombre)

# Llamar a la función para mostrar los nombres
mostrar_nombres()




