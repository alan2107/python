# Ejercicio 1:
# Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
# sueldo para esa persona.

nombre = input("Ingrese su nombre: ")
sueldo = float(input("Ingrese su sueldo: "))

# Incrementar el sueldo en un 10%
sueldo_incrementado = sueldo * 1.10

# Calcular el aumento de sueldo
aumento = sueldo_incrementado - sueldo

# Informar el aumento de sueldo para esa persona
print(f"¡Hola {nombre}! Su sueldo ha sido incrementado en un 10%.")
print(f"Antes tenía un sueldo de ${sueldo:.2f} y ahora tiene un sueldo de ${sueldo_incrementado:.2f}.")
print(f"El aumento de sueldo es de ${aumento:.2f}.")