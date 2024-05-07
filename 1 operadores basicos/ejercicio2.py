# Ejercicio 2:
# Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
# adolescente (entre 13 y 17 años) o niño (menor a 13 años).

# Pedir la edad
edad = int(input("Ingrese su edad: "))

# Verificar la edad y dar el resultado correspondiente
if edad >= 18:
    print("Eres mayor de edad.")
elif 13 <= edad <= 17:
    print("Eres adolescente.")
else:
    print("Eres un niño.")