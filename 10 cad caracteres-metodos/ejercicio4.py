'''
Ejercicio 4: Desarrollar una función que convierta los elementos de lista_peli en una
cadena y muestre:
ej. "Se recomienda ver "Matrix", "El Padrino" y "Titanic" "" para cada elemento
lista_peli = [
["Matrix", "El Padrino", "Titanic"],
["Forrest Gump", "Pulp Fiction", "Gladiador"],
["Blade Runner", "El Rey León", "Volver al Futuro"],
["La La Land", "El Gran Lebowski", "Blade Runner"],
["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
["Harry Potter", "Forrest Gump", "Pulp Fiction"],
["Titanic", "Star Wars", "El Señor de los Anillos"],
["The Truman Show", "The Shape of Water", "The Big Lebowski"],
["Forrest Gump", "The Godfather", "Goodfellas"],
["The Terminator", "The Sixth Sense", "The Great Gatsby"]
]
'''

def recomendar_peliculas(lista_peli):
    """
    Esta función convierte los elementos de una lista de películas en una cadena y muestra una recomendación.

    Argumentos:
    lista_peli (list): Una lista de listas, donde cada sublista contiene nombres de películas.

    Retorna:
    str: La cadena con la recomendación de películas.
    """
    recomendacion = "Se recomienda ver "
    for peliculas in lista_peli:
        recomendacion += '"' + '", "'.join(peliculas) + '"'
        recomendacion += " y "
    # Eliminamos el último " y " y añadimos las comillas finales
    recomendacion = recomendacion[:-3] + '""'
    return recomendacion

# Lista de películas
lista_peli = [
    ["Matrix", "El Padrino", "Titanic"],
    ["Forrest Gump", "Pulp Fiction", "Gladiador"],
    ["Blade Runner", "El Rey León", "Volver al Futuro"],
    ["La La Land", "El Gran Lebowski", "Blade Runner"],
    ["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
    ["Harry Potter", "Forrest Gump", "Pulp Fiction"],
    ["Titanic", "Star Wars", "El Señor de los Anillos"],
    ["The Truman Show", "The Shape of Water", "The Big Lebowski"],
    ["Forrest Gump", "The Godfather", "Goodfellas"],
    ["The Terminator", "The Sixth Sense", "The Great Gatsby"]
]

# Mostramos la recomendación de películas
print(recomendar_peliculas(lista_peli))