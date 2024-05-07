#Funciones recursiva para calcular la potencia de un numero
def potencia(base, exponente):
    #caso base: si el exponente es 0, el resultado es 1
    if exponente == 0:
        return 1
    #caso recursivo: calculamos la potencia recursivamente
    else:
        return base * potencia(base, exponente - 1)
    
#probando la funcion con una besa y un exponente
base = 2
exponente = 3
print("la potencia de", base, "elevado a", exponente, "es: ", potencia(base, exponente))

# Ejercicio:
# ● Numero primos son:
# ● Número entero positivo mayor que el número uno y que
# ● solo puede ser divisible sin resto por el número uno y por el mismo.
# ● Los primeros números primos son:
# 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47, ...
# ● Realizar un programa que solicite un número y a través de una función
# recursiva determine si el número es primo.

def es_primo(n, divisor=None):
    if divisor is None:
        divisor = n - 1  # Empezamos con el divisor igual a n - 1
    
    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    elif divisor == 1:
        return True  # Si llegamos a 1 como divisor y no hubo ningún divisor antes, es primo
    elif n % divisor == 0:
        return False  # Si n es divisible por el divisor, no es primo
    else:
        return es_primo(n, divisor - 1)  # Llamada recursiva con el siguiente divisor

# Solicitar al usuario un número para verificar si es primo
numero = int(input("Ingrese un número entero positivo: "))

# Verificar si el número ingresado es primo utilizando la función es_primo
if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")

#NUMERO FACTORIAL

# Realizar un programa que solicite un número y a través de una función
# recursiva determine su factorial.
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        print("El factorial de números negativos no está definido.")
    else:
        return n * factorial(n-1)

def main():
    num = input("Ingresa un número para calcular su factorial: ")
    if num.isdigit():
        num = int(num)
        if num < 0:
            print("El factorial de números negativos no está definido.")
        else:
            print("El factorial de", num, "es:", factorial(num))
    else:
        print("Debes ingresar un número entero válido.")

if __name__ == "__main__":
    main()