from biblioteca import *

mercaderia = [['botellas', 3, [1, 2]],
              ['frascos', 8, [1, 4]],
              ['fideos', 4, [2, 3]],
              ['leche', 6, [3, 4]]]

bandera = False

while True:
    menu()
    opcion= input("Ingrese una opcion: ")

    if opcion == "1":
        alta_producto(mercaderia)
        bandera = True
    elif opcion == "2":
        if bandera == False:
            baja_producto(mercaderia)
        else:
            print("Error.. Primero da de alta el producto")
    elif opcion == "3":
        if bandera == False:
            modificar_producto(mercaderia)
        else:
            print("Error: primero da de alta el producto")
    elif opcion == "4":
        listar_productos(mercaderia)
    elif opcion == "5":
        ordenar_por_nombre(mercaderia)
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")