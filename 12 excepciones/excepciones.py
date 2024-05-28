try:
    dividendo = 4
    divisor = 4
    resultado = dividendo / divisor
    print(resultado)
except ZeroDivisionError:
    print("no se puede dividir por cero")
except NameError:
    print('la variable no existe')
except TypeError:
    print('Error de tipo')
else: #Opcional
    print('Calulo fue exitoso')
finally:
    print('por bien o por mal, termina el codigo')