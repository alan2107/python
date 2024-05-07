def mostrar_mercaderia():
    for merca in mercaderia:
        print(merca)
    print("\n")


mercaderia = [['botellas', 3, [1, 2]],
              ['frascos', 8, [1, 4]],
              ['fideos', 4, [2, 3]],
              ['leche', 6, [3, 4]]]


#nuevo producto aceite, 10, en [3,2]
mercaderia.append(["aceite", 10, [3,2]])

mostrar_mercaderia()

#vender 2 aceites
productos_a_vender = "aceite"

# for producto in mercaderia:
#     if producto[0] == productos_a_vender:
#         producto[1] -= productos_a_vender

#mover los fideos a 2,4

mercaderia[2][2][1] = 4
mostrar_mercaderia()