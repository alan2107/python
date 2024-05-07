'''
Ejercicio 10:
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres
Ejemplo:
nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = ["m","m","f","m","f"]
nota = [6,8,10,8,5]
'''
# declaro listas
nombres = []
sexo = []
notas = []

#recorro y valido entrada de usuario
for i in range(5):
    nombre = input("Ingrese nombre del alumno {}: ".format(i + 1))
    while not nombre.isalpha():
        print("el nombre es invalido.. intente nuevamente: ")
        nombre = input("Ingrese nombre del alumno {}: ".format(i + 1))
    
    sexo_alumno = input("Ingrese el sexo alumno con (f/m): ")
    while sexo_alumno != "f" and sexo_alumno != "m":
        print("El sexo no es valido.. Ingrese el sexo nuevamente")
        sexo_alumno = input("Ingrese el sexo alumno con (f/m): ")

    nota_alumno = float(input("Ingrese nota de alumno: "))
    while nota_alumno < 0 or nota_alumno > 10:
        print("la nota no es valida.. Ingrese la nota nuevamente")
        nota_alumno = float(input("Ingrese nota de alumno: "))

    #una vez todo validado, agrego cada elemento a la lista
    nombres.append(nombre)
    sexo.append(sexo_alumno)
    notas.append(nota_alumno)

    #declaro variables 
    nota_min_hombre = 10
    total_notas_mujeres = 0
    cantidad_mujeres = 0

    #encuentro el hombre con nota mas baja
    for i in range(5):
        if sexo[i] == "m":
            if notas[i] < nota_min_hombre:
                nota_min_hombre = notas[i]
                nombre_min_hombre = nombres[i]
        else:
            total_notas_mujeres += notas[i]
            cantidad_mujeres += 1

#saco el promedio de notas de las mujeres

promedio_notas_mujeres = cantidad_mujeres / total_notas_mujeres

#muestro el hombre con nota mas baja y el promedio de notas de mujeres
print("el nombre con nota mas bajas de los hombres es: ", nombre_min_hombre)
print("El promedio de notas de todas las mujeres es: ", promedio_notas_mujeres)