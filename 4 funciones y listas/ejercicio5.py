""" Ejercicio 5: Dadas las siguientes listas:
Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Ped
ro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que reciba por parámetro la lista de edades, busque a las
personas de menor edad (puede ser más de una) y las retorne. El programa
principal deberá mostrar nombre y edad de los menores. """

def personas_menor_edad(nombres, edades):
    menor_edad = min(edades)
    personas_menores = [(nombres[i], edades[i]) for i in range(len(nombres)) if edades[i] == menor_edad]
    return personas_menores

# Listas de nombres y edades
nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]

# Obtener personas de menor edad
menores = personas_menor_edad(nombres, edades)

# Mostrar nombres y edades de los menores
print("Personas de menor edad:")
for nombre, edad in menores:
    print(f"Nombre: {nombre}, Edad: {edad}")