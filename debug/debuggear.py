from os import system
system("cls")

def factorial(n): #el producto de 1 hasta n
    if n < 0:
        raise ValueError("El numero debe ser no negativo")
    elif n == 0:
        return 1
    else: 
        return n * factorial(n - 1)
    
print(factorial(3))
""" def a():
    lista = [1,6,3,7,4]
    for i in range(len(lista)):
        if(lista[i] > 3):
            if(lista[i] > 50 ): return True
            else: return True """