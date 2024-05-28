import csv

def  parse_csv(nombre_archivo:str)->list:
    lista  = []
    #archivo = open(nombre_archivo, 'r)  #si se usa este metodo dsp hay que cerrarlo
    with open(nombre_archivo, 'r') as archivo:
        for e_linea in archivo:
            lista.append(e_linea) #le agrego la linea que voy leyendo
    #archivo.close()
    return lista

#convierto los datos a memoria en una lista de diccionarios
def  parse_csv_a_diccionario(nombre_archivo:str)->list:
    lista_rta  = []
    with open(nombre_archivo, 'r') as archivo:
        for e_linea in archivo:
            lista_temporaria = e_linea.split(",")
            #creo el diccionario
            tema = {}
            tema["title"] = lista_temporaria[0]
            tema["views"] = lista_temporaria[1]
            tema["length"] = lista_temporaria[2]
            tema["img_url"] = lista_temporaria[3]
            tema["url"] = lista_temporaria[4]
            tema["date"] = lista_temporaria[5]
            lista_rta.append(tema)
    return lista_rta

def generar_csv(nombre_archivo:str, lista:list):
    with open(nombre_archivo, "w") as archivo:
        for e_tema in lista:
            linea = "{0},{1},{2},{3},{4},{5}"
            linea = linea.format(
                                e_tema["title"],
                                e_tema["views"],
                                e_tema["length"],
                                e_tema["img_url"],
                                e_tema["url"],
                                e_tema["date"])
            print(linea)
            archivo.write(linea)

#PROGRAMA PRINCIPAL

#la primer funcion
""" lista = []
lista = parse_csv("data.csv")
print(lista[0]) """

#segunda funcion
""" lista = parse_csv_a_diccionario("data.csv")
print(lista[0]) """

#tercera funcion
lista = parse_csv_a_diccionario("data.csv")
generar_csv("data_salida.csv", lista)




