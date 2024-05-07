#SIN LAMBDA

def identificar_par(num)->str:
    result = "espar" if num %2 == 0 else "No es par"
    return result

respuesta = identificar_par(3)
print(respuesta)

#CON LAMBDA
print((lambda num: "es par" if num %2 == 0 else "NO es par")(3))