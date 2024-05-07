def mostrar():
    for contacto in contactos:
        print(contacto)
    print("\n")

# nombres = ["Ana", "Juan", "Sol","Luis", "Roberto"]
# edades = [23, 45, 34, 23, 46]
# telefono = [[123,134], [453,233], [232,234], [234], [274]]

contactos = [["Ana",23 , [123,134]],
             ["Juan",45, [453,233]],
             ["Sol",34,[232,234]],
             ["Luis",23 ,[234]],
             ["Roberto",46, [274]]
             ]

mostrar()
#Borrar a roberto

contactos.pop(4)
mostrar()

#borrar el2do telefono de sol
contactos[2][2].pop(1)
print("Borrrar el segundo telefono de sol")
mostrar()

#Agregamos un nuevo contacto
contactos.append(["Roberto", 46, [321]])
print("Agregamos un nuevo contacto")
mostrar()

#Agregar un año a Luis que fue su cumple
contactos[3][1] += 1
print("Agregamos un año a Luis")
mostrar()

#Ordenamos por nombres
for i in range(len(contactos)-1):
    for j in range(i+1, len(contactos)):
        if contactos[i][0] > contactos[j][0]:
            auxc = contactos[i]
            contactos[i] = contactos[j]
            contactos[j] = auxc

mostrar()

def mostrar1():
    for merca in mercaderia:
        print(merca)
    print("\n")


mercaderia = [['botellas', 3, [1, 2]],
            ['frascos', 8, [1, 4]],
            ['fideos', 4, [2, 3]],
            ['leche', 6, [3, 4]]]


#nuevo producto aceite, 10, en [3,2]
mercaderia.append(["aceite", 10, [3,2]])

mostrar1()

#vender 2 aceites
productos_a_vender = "aceite"

# for producto in mercaderia:
#     if producto[0] == productos_a_vender:
#         producto[1] -= productos_a_vender

#mover los fideos a 2,4

mercaderia[2][2][1] = 4
mostrar1()
#-------------------------------------------------------------------------
def mostrar2():
    for cajon in estanteria:
        for fila in cajon:
            print(fila[0],fila[1])
    print("\n")

estanteria =[[["to12",65], ["to16",86], ["to20", 65], ["to25", 45]],
             [["to30",68], ["to35", 73], ["to40",85], ["to45", 89]],
             [["ta4", 58], ["ta5",48], ["ta6", 64], ["ta7",96]],
             [["ta8", 36], ["ta10", 72], ["ta12", 78], ["ta14", 71]]
]
#Reponer mercadería (productos existentes)
producto = input("Ingrese el producto a reponer: ")
cantidad = int(input("ingrese cantidad"))

mostrar2()
for cajon in estanteria:
    for fila in cajon:
         if fila[0] == producto:
             fila[1] += cantidad

mostrar2()
