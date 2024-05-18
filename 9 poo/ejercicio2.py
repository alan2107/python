'''
Ejemplo: Clase para representar un Libro
Crear una clase Libro que tenga las características título, autor y año de publicación. Del libro se
debe poder obtener información, mostrando por mensaje todos sus datos. Se debe crear la clase
e implementarla.
'''

class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def obtener_informacion(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nAño de publicación: {self.año_publicacion}"

# Crear una instancia de Libro
libro1 = Libro("CONTRA EL RUMBO", "MARCOS PEREYRA", 2010)

# Obtener información del libro
informacion_libro1 = libro1.obtener_informacion()
print(informacion_libro1)