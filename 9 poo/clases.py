class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad}años.")


#crear un objeto de la clase Persona
juan = Persona(nombre= "Juan", edad = 30)
#acceder a los atributos y llamar al metodo
print(juan.nombre)
print(juan.edad)
juan.saludar()

ana = Persona(nombre= "Ana", edad= 25)

print(ana.nombre)

#-------------------------------- HERENCIA--------------------------------------

