def mostrar_estanteria():
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

mostrar_estanteria()
for cajon in estanteria:
    for fila in cajon:
         if fila[0] == producto:
             fila[1] += cantidad

mostrar_estanteria()