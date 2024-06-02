def menu():    
    print("Menú de Opciones:")     
    print("A- Listar ordenado por Nombre. Lista todos los datos de cada superhéroe ordenados por Nombre de manera ascendente.")     
    print("B- Listar Masculinos débiles. Recorrer la lista y determinar cuál es el superhéroe más débil degénero M.")     
    print("C- Cantidad por color de ojos. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")     
    print("D- Listar por color de Pelo. Listar todos los superhéroes agrupados por color de pelo")     
    print("E- Listar inteligencia. Listar todos los superhéroes agrupados por tipo de inteligencia")     
    print("F- Listar Promedio. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquiergénero) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino")    
    print("G- Asignar IMC. Calcular el índice de masa corporal de cada superhéroe y guardarla en un nuevo campo. Se deberá hacer uso de una función lambda que asignará a cada superhéroe el IMC calculado.")     
    print("H- Salir")

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

#----------------------------------------------------------------------------------------------------------------
def ordenar_por_nombre(lista_personaje:list):
    '''
    lista todos los personajes ordenados por nombre de manera ascendente.
    
    argumentos:
    lista_personajes (list): lista de diccionarios que representan los personajes

    regresa:
    list : lista de personajes ordenada por nombre

    '''
    
    return sorted(lista_personaje, key=lambda x: x['nombre'])


def listar_masculinos_debiles(lista_personajes:list):
    '''
    Determina el superheroe masculino mas debil.

    return: dict: el personaje masculino mas debil
    '''
    masculinos = [superheroe for superheroe in lista_personajes if superheroe['genero'] == 'M']
    return min(masculinos, key=lambda x: int(x['fuerza']))
    

def calcular_cantidad_color_de_ojos(lista_personajes:list):
    '''
    determina la cantidad de superheroes por cada color de ojos.

    return: un diccionario con los colores de ojos como claves y la cantidad de personajes como valores

    '''
    color_ojos_counts = {}
    for superheroe in lista_personajes:
        color_ojos = superheroe['color_ojos']
        color_ojos_counts[color_ojos] = color_ojos_counts.get(color_ojos, 0) + 1
    return color_ojos_counts

def listar_por_color_pelo(lista_personajes:list):
    '''
    lista todos los personajes agrupados por color de pelo

    return un diccionario con los colores de pelo como claves y lista de personajes como valores

    '''
    superheroe_por_color_pelo = {}
    for superheroe in lista_personajes:
        color_pelo = superheroe['color_pelo']
        if color_pelo not in superheroe_por_color_pelo:
            superheroe_por_color_pelo[color_pelo] = []
        superheroe_por_color_pelo[color_pelo].append(superheroe)
    return superheroe_por_color_pelo
        

def listar_inteligencia(lista_personajes:list):
    '''
    lista todos los personajes agrupados por tipo de inteligencia
    '''
    superheroes_por_inteligencia = {}
    for superheroe in lista_personajes:
        inteligencia = superheroe['inteligencia']
        if inteligencia not in superheroes_por_inteligencia:
            superheroes_por_inteligencia[inteligencia] = []
        superheroes_por_inteligencia[inteligencia].append(superheroe)
    return superheroes_por_inteligencia

def listar_promedio(lista_personajes:list):
    '''
    Muestra nombre y peso de los superheroes cuya fuerza supera el promedio de fuerza de todas las superheroes de genero femenino

    return lista de tuplas con el nombre y peso de los personajes que cumplen con la condicion

    '''
    fuerza_promedio_femenina = sum(int(superheroe['fuerza']) for superheroe in lista_personajes if superheroe['genero'] == 'F') / len([superheroe for superheroe in lista_personajes if superheroe['genero']=='F'])
    return [(superheroe['nombre'], superheroe['peso']) for superheroe in lista_personajes if int(superheroe['fuerza']) > fuerza_promedio_femenina]

def agregar_imc(lista_personajes:list):
    """
    calcula el indice de masas corporal (IMC) de cada superheroe y lo guarda en un nuevo campo.

    return lista de personaje con el campo IMC aniadido.
    """

    for superheroe in lista_personajes:
        altura_metros = float(superheroe['altura']) / 100
        peso = float(superheroe['peso'])
        imc = peso / (altura_metros ** 2)
        superheroe['IMC'] = imc
    return lista_personajes

def presionar_tecla():
    import msvcrt
    print("Pulsa una tecla para volver al menú")
    msvcrt.getch()  # Espera a que el usuario presione una tecla

def limpiar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear') 
#print("{:<40} {:<40} {:<20} {:<15}".format(col1, col2, col3, col4))