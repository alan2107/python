'''
Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven
'''

edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]

edad_mas_joven = edades[0]
indice_persona_mas_joven = 0

for edad in range(len(edades)):
    if edades[edad] < edad_mas_joven:
        edad_mas_joven = edades[edad]
        indice_persona_mas_joven = edad
    
nombre_persona_mas_joven = nombre[indice_persona_mas_joven]

print("la persona mas joven es: ", nombre_persona_mas_joven)