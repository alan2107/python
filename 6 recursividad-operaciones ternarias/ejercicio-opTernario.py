""" Escribir un programa con operadores ternarios que determine si un número ingresado
por el usuario es par. """

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Usar un operador ternario para determinar si el número es par
resultado = "par" if numero % 2 == 0 else "impar"

# Imprimir el resultado
print(f"El número {numero} es {resultado}.")