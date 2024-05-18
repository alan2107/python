'''
Ejemplo: Clase para representar una Calculadora
Crear una clase Calculadora que pueda calcular suma, resta, multiplicación y división. Se debe
crear la clase e implementarla.
'''
class Calculadora:
    def suma(self, num1, num2):
        return num1 + num2

    def resta(self, num1, num2):
        return num1 - num2

    def multiplicacion(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            return "Error: No se puede dividir por cero."
        else:
            return num1 / num2

calculadora = Calculadora()

resultado_suma = calculadora.suma(5, 3)
resultado_resta = calculadora.resta(5, 3)
resultado_multiplicacion = calculadora.multiplicacion(5, 3)
resultado_division = calculadora.division(5, 3)

print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_multiplicacion)
print("División:", resultado_division)



