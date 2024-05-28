import json

def menu():    
    print("Menú de Opciones:")     
    print("A- leer archivo JSON")     
    print("B- Ordenar heroes por alguna de las claves numericas (altura, peso y fuerza) de manera ascendente")     
    print("C- Guardar el listado ordenado en un CSV. pedir el nombre del archivo al usuario")     
    print("D- Salir")     

def leer_jason(archivo, clave_lista):
    try:
        with open(archivo, 'r') as archivo:
            datos = json.load(archivo)  
            if clave_lista in datos:
                retorno = datos[clave_lista]
            else:
                retorno =  False
    except FileNotFoundError:
        retorno = False
    except json.JSONDecodeError:
        retorno = False
    return retorno

def  guardar_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)
            print(f"Se creo el archivo: {nombre_archivo}")
            retorno = True
    except Exception as e:
        print(f"Error al crear el archivo: {nombre_archivo}")
        retorno = False
        return retorno


def generar_csv(nombre_archivo, lista_heroes)->list:
    if not lista_heroes:
        retorno = False
    
    #obtener los encabezados de las claves del primer heroe
    encabezados = lista_heroes[0].keys()
    contenido_csv = ','.join(encabezados) + '\n'

    #construyo filas del csv
    for heroe in lista_heroes:
        fila = []
        for encabezado in encabezados:
            fila.append(str(heroe[encabezado]))
        contenido_csv += ','.join(fila) + '\n'

    if guardar_archivo(nombre_archivo, contenido_csv):
        retorno = True
    else:
        retorno = False
    return retorno

def opcion_leer_json():
    ruta_archivo = input("Ingrese la ruta del archivo JSON: ")
    clave_lista = input("Ingrese la clave de la lista a leer: ")
    lista_heroes = leer_jason(ruta_archivo, clave_lista)
    if lista_heroes:
        print("Lista de heroes leida correctamente.")
    else:
        print("Error al leer el archivo JSON o la clave no existe.")
    return lista_heroes

def opcion_ordenar_heroes(lista_heroes):
    if not lista_heroes:
        print("La lista de heroes esta vacia. Lea primero un archivo JSON.")
        retorno = []
    
    clave = input("Ingrese la clave numerica por la que desear ordenar(altura, peso, fuerza): ")
    if clave not in lista_heroes[0]:
        print("clave no valida.")
        retorno = lista_heroes
    
    lista_ordenada = sorted(lista_heroes, key=lambda x: x[clave])
    print(f"Lista ordenada por {clave} de manera ascendente.")
    retorno = lista_ordenada
    return retorno

def opcion_guardar_csv(lista_heroes):
    if not lista_heroes:
        print("La lista de heroes esta vacia. No se puede guardar.")
    
    nombre_archivo_csv = input("Ingrese el nombre del archivo CSV a guardar: ")
    if generar_csv(nombre_archivo_csv, lista_heroes):
        print("Lista guardada en CSV correctamente")
    else:
        print("Error al guardar el archivo CSV.")
