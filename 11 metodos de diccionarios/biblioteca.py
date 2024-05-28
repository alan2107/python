def menu():    
    print("Menú de Opciones:")     
    print("1- Listar los alumnos por orden ascendente de apellido")     
    print("2- Obtener el promedio de notas para cada estudiante")     
    print("3- Listar estudiantes de Ingenieria en Informatica")     
    print("4- Obtener un promedio de edad de los estudiantes")     
    print("5- Informar el alumno con mayor promedio de notas")     
    print("6- Listar alumnos del Club de Informatica con sus promedios")    
    print("7- Listar alumnos más jóvenes")     
    print("0- Salir")

def mostrar_uno(mercaderia, pos):
    print(mercaderia[pos])

def mostrar_todos(mercaderia, pos):
    for i in range(len(mercaderia)):
        mostrar_uno(i)
    print("\n")



def toma_de_datos():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))

    return nombre, cantidad

def alta_de_producto(mercaderia:list):
    producto = input("Ingrese el producto a reponer: ")
    cantidad = int(input("Ingrese la cantidad que quiere agregar: "))
    for i in range(len(mercaderia)):
        for j in range(len(mercaderia)):
            if mercaderia[i][j][0] == producto:
                mercaderia[i][j][1] += cantidad
    

def baja_producto(mercaderia:list):
    # Buscar el producto y eliminarlo si existe
    mercaderia = input("Ingrese que producto fue vendido: ")
    cantidad = int(input("Ingrese la cantidad vendida: "))

    for i in range(len(mercaderia)):
        for j in range(len(mercaderia)):
            if mercaderia[i][j][0] == mercaderia:
                if mercaderia[i][j][1] > cantidad:
                    mercaderia[i][j][1] -= cantidad
                else:
                    print("No posees la cantidad necesario de mercaderia")

def modificar_producto(mercaderia, nombre, nueva_cantidad, nueva_ubicacion):
    # Buscar el producto y modificarlo si existe
    for producto in mercaderia:
        if producto[0] == nombre:
            producto[1] = nueva_cantidad
            producto[2] = nueva_ubicacion
            print("Producto modificado con éxito.")
        else:
            print("El producto no existe.")

def listar_productos(mercaderia):
    print("Listado de productos:")
    for producto in mercaderia:
        print(f"Nombre: {producto[0]}, Cantidad: {producto[1]}, Ubicación: {producto[2]}")

def ordenar_por_nombre(mercaderia):
    #implementar un algoritmo de ordenamiento manual
    for i in range(len(mercaderia)-1):
        for j in range(i+1, len(mercaderia)):
            if mercaderia[i][0] > mercaderia[j][0]:
                aux_mercaderia = mercaderia[i][0]
                mercaderia[i][0] = mercaderia[j][0]
                mercaderia[j][0] = aux_mercaderia

    print("Listado de productos ordenados por nombre:")
    for producto in mercaderia:
        print(f"Nombre: {producto[0]}, Cantidad: {producto[1]}, Ubicacion: {producto[2]}")
#---------------------------------------------------------------------------------------------------
def imprimir_cuadro(estudiantes:list):
    """
    Imprime un cuadro con los datos de los estudiantes usando tabulaciones y saltos de linea.
    """
    #Encabezados
    encabezado = "Legajo\tNombre\tApellido\tEdad"
    print(encabezado)
    print("-" * len(encabezado.expandtabs(16))) #linea de separacion

def comparar_estudiantes(estudiante):
    '''
    funcion que retorna una tupla con el apellido y nombre del estudiante para usar en la funcion de ordenamiento.
    '''
    return (estudiante["apellido"], estudiante["nombre"])

def listar_alumnos_ordenados(estudiantes:list):
    """
    Lista los alumnos ordenados por apellido y nombre.
    """
    estudiantes_ordenados = sorted(estudiantes, key=comparar_estudiantes)
    imprimir_cuadro(estudiantes_ordenados)
    for estudiante in estudiantes_ordenados:
        print(f"{estudiante['legajo']}\t{estudiante['nombre']}\t{estudiante['apellido']}\t{estudiante['edad']}")

def calcular_promedio(valores:list):
    '''
    calcula el promedio de una lista de valores
    '''
    if not valores:
        return 0
    return sum(valores) / len(valores)

def obtener_promedio_notas(estudiantes:list):
    '''
    obtiene el promedio de notas para cada estudiante.
    '''
    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante['notas'])
        print(f"Legajo: {estudiante['legajo']}\tNombre: {estudiante['nombre']}\tPromedio: {promedio:.2f}")

def listar_estudiantes_ingenieria(estudiantes:list):
    """
    Lista los estudiantes que cursan el programa de "Ingenieria en Informatica".
    """
    for estudiante in estudiantes:
        if estudiante['programa']['nombre'] == "Ingenieria en Informatica":
            print(f"Legajo: {estudiante['legajo']}, Nombre: {estudiante['nombre']}, Apellido: {estudiante['apellido']}, Edad: {estudiante['edad']}")

def obtener_promedio_edad(estudiantes):
    """
    Obtiene el promedio de edad de los estudiantes.
    """
    total_edad = sum(estudiante['edad'] for estudiante in estudiantes)
    promedio_edad = total_edad / len(estudiantes)
    print(f"Promedio de edad: {promedio_edad:.2f}")

def alumno_mayor_promedio(estudiantes:list):
    """
    Informa el alumno con mayor promedio de notas.
    """
    mayor_promedio = None
    mejor_estudiante = None
    for estudiante in estudiantes:
        promedio = sum(estudiante['notas']) / len(estudiante['notas'])
        if mayor_promedio is None or promedio > mayor_promedio:
            mayor_promedio = promedio
            mejor_estudiante = estudiante
    print(f"Nombre: {mejor_estudiante['nombre']}, Apellido: {mejor_estudiante['apellido']}, Promedio: {mayor_promedio:.2f}")

def listar_alumnos_club_informatica(estudiantes:list):
    """
    Lista los alumnos que forman parte del grupo "Club de Informatica" con sus respectivos promedios.
    """
    for estudiante in estudiantes:
        if any(grupo['nombre'] == "Club de Informatica" for grupo in estudiante.get('grupos', [])):
            promedio = sum(estudiante['notas']) / len(estudiante['notas'])
            print(f"Nombre: {estudiante['nombre']}, Apellido: {estudiante['apellido']}, Promedio: {promedio:.2f}")

def listar_alumnos_mas_jovenes(estudiantes:list):
    """
    Lista los alumnos más jóvenes.
    """
    menor_edad = min(estudiante['edad'] for estudiante in estudiantes)
    for estudiante in estudiantes:
        if estudiante['edad'] == menor_edad:
            print(f"Legajo: {estudiante['legajo']}, Nombre: {estudiante['nombre']}, Apellido: {estudiante['apellido']}, Programa: {estudiante['programa']['nombre']}")