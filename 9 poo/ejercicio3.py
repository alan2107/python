'''
Ejemplo: Clase para representar un Rectángulo
Crear una clase rectángulo que tenga las características base y altura. Del rectángulo se debe
poder calcular el área y el perímetro. Se debe crear la clase e implementarla.
'''
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

rectangulo1 = Rectangulo(5, 3)

area_rectangulo1 = rectangulo1.calcular_area()
perimetro_rectangulo1 = rectangulo1.calcular_perimetro()

print("Área del rectángulo:", area_rectangulo1)
print("Perímetro del rectángulo:", perimetro_rectangulo1)