def menu():
    print("Menú de opciones:")
    print("1-Alta de productos")
    print("2-Baja de productos")
    print("3-Modificar productos")
    print("4-Listar productos")
    print("5-Lista de productos ordenado por nombre")
    print("6-Salir")

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

def alta_producto(mercaderia):
    nombre = []
    cantidad = []
    ubicacion = []
    toma_de_datos()
    # Verificar si el producto ya existe
    for producto in mercaderia:
        if producto[0] == nombre:
            print("El producto ya existe.")
        else:
            #agregar el nuevo producto
            mercaderia.append([nombre, cantidad, ubicacion])
            print("Producto agregado con exito")
    

def baja_producto(mercaderia, nombre):
    # Buscar el producto y eliminarlo si existe
    for producto in mercaderia:
        if producto[0] == nombre:
            mercaderia.remove(producto)
            print("Producto eliminado con éxito.")
        else:
            print("El producto no existe.")

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
