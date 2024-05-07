'''
ejercicio 5
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%
-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%
-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.
Validar el ingreso de datos
'''

costo_base = 15000

while True:
    estacion = input("Ingrese una estacion (invierno, otoño, primavera, verano): ").lower()
    if estacion == "invierno" or estacion == "otoño" or estacion == "primavera" or estacion == "verano":
        break
    else:
        print("Error.. Porfavor ingrese una estacion valida.")

while True:
    localidad = input("Ingrese una localidad (Bariloche, Cataratas, Mar del Plata, Cordoba): ").capitalize()
    if localidad == "Bariloche" or localidad == "Cataratas" or localidad == "Mar del plata" or localidad == "Cordoba":
        break
    else:
        print(" Error.. por favor ingrese localidad valida.")

precio_final = None

match estacion:
    case "invierno":
        match localidad:
            case "Bariloche":
                precio_final = costo_base * 1.2
            case "Cataratas", "Cordoba":
                precio_final = costo_base * 0.9
            case "Mar del plata":
                precio_final = costo_base * 0.8
    case "verano":
        match localidad:
            case "Bariloche": 
                precio_final = costo_base * 0.8
            case "Cataratas", "Cordoba":
                precio_final = costo_base * 1.2
            case "Mar del plata":
                precio_final = costo_base * 1.2
    case "otoño", "primavera":
        match localidad:
            case "Mar del plata", "Bariloche", "Cataratas":
                precio_final = costo_base * 1.1
            case "Cordoba":
                precio_final = costo_base

if precio_final is not None:
    print("El precio final del viaje es $: ", precio_final)