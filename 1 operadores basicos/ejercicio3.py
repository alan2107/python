""" Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos. """

# Inicializamos variables para almacenar los resultados
cantidad_pares = 0
cantidad_impares = 0
menor_numero = None
mayor_par = None
suma_positivos = 0
producto_negativos = 1

# Ingresar 5 números enteros distintos de cero
for i in range(5):
    num = int(input(f"Ingrese el número {i+1}: "))
    while num == 0:
        num = int(input("El número debe ser distinto de cero. Ingrese otro número: "))

    # Contar la cantidad de pares e impares
    if num % 2 == 0:
        cantidad_pares += 1
        # Determinar el mayor número par
        if mayor_par is None or num > mayor_par:
            mayor_par = num
    else:
        cantidad_impares += 1

    # Calcular el menor número ingresado
    if menor_numero is None or num < menor_numero:
        menor_numero = num

    # Calcular suma de los positivos y producto de los negativos
    if num > 0:
        suma_positivos += num
    else:
        producto_negativos *= num

# a. Cantidad de pares e impares
print(f"a. Cantidad de pares: {cantidad_pares}")
print(f"   Cantidad de impares: {cantidad_impares}")

# b. El menor número ingresado
print(f"b. El menor número ingresado: {menor_numero}")

# c. De los pares el mayor número ingresado
print(f"c. De los pares el mayor número ingresado: {mayor_par if mayor_par is not None else 'No hay números pares'}")

# d. Suma de los positivos
print(f"d. Suma de los positivos: {suma_positivos}")

# e. Producto de los negativos
print(f"e. Producto de los negativos: {producto_negativos}")