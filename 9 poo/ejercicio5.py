'''
Ejemplo: Herencia de clases
Crear una clase Animal que tenga la característica nombre. La clase Perro que herede de Animal
las características y realice el sonido “guau guau”. La clase Gato que herede de Animal las
características y realice el sonido “Miau”. Del gato y el perro se debe poder mostrar el sonido que
realizan. Se debe crear la clase e implementarla.
'''

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def ladra(self):
        return "guau guau"

class Gato(Animal):
    def maulla(self):
        return "Miau"

# Creo instancia de Perro y Gato
perro1 = Perro("toby")
gato1 = Gato("ruby")

# Muestro el sonido que hacen
print(f"{perro1.nombre} hace: {perro1.ladra()}")
print(f"{gato1.nombre} hace: {gato1.maulla()}")