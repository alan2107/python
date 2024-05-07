import listas_personas

def menu():
    print("Menú de opciones:")
    print("1- Importar listas")
    print("2- Listar los datos de los usuarios de México")
    print("3- Listar los nombre, mail y teléfono de los usuarios de Brasil")
    print("4- Listar los datos del/los usuario/s más joven/es")
    print("5- Obtener un promedio de edad de los usuarios")
    print("6- De los usuarios de Brasil, listar los datos del usuario de mayor edad")
    print("7- Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000")
    print("8- Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años")
    print("9-Listar los datos de los usuarios de México ordenados por nombre")
    print("10-Listar los datos del/los usuario/s más joven/es ordenados por edad de manera ascendente (Si la edad se repite, ordenar por nombre de manera ascendente)")
    print("11-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 ordenado por nombre y edad de manera descendente")
    print("12-Salir")


def importar_listas():
    global nombres, telefonos, mails, address, postalZip, region, country, edades
    nombres = listas_personas.nombres
    telefonos = listas_personas.telefonos
    mails = listas_personas.mails
    address = listas_personas.address
    postalZip = listas_personas.postalZip
    region = listas_personas.region
    country = listas_personas.country
    edades = listas_personas.edades

def listar_usuarios_mexico():
    print("Usuarios de México:")
    for i in range(len(nombres)):
        if country[i] == "Mexico":
            print(f"Nombre: {nombres[i]}, Teléfono: {telefonos[i]}, Email: {mails[i]}, Dirección: {address[i]}, Código Postal: {postalZip[i]}, Región: {region[i]}, País: {country[i]}, Edad: {edades[i]}")

def listar_datos_usuarios_brasil():
    print("Usuarios de Brasil:")
    for i in range(len(nombres)):
        if country[i] == "Brazil":
            print(f"Nombre: {nombres[i]}, Teléfono: {telefonos[i]}, Email: {mails[i]}")

def listar_usuario_mas_joven():
    edad_minima = min(edades)
    print("Usuario/s más joven/es:")
    for i in range(len(nombres)):
        if edades[i] == edad_minima:
            print(f"Nombre: {nombres[i]}, Teléfono: {telefonos[i]}, Email: {mails[i]}, Dirección: {address[i]}, Código Postal: {postalZip[i]}, Región: {region[i]}, País: {country[i]}, Edad: {edades[i]}")

def promedio_edad_usuarios():
    promedio = sum(edades) / len(edades)
    print(f"Promedio de edad de los usuarios: {promedio}")

def listar_usuario_mayor_edad_brasil():
    edad_maxima = max(edades)
    print("Usuario/s de Brasil de mayor edad:")
    for i in range(len(nombres)):
        if country[i] == "Brazil" and edades[i] == edad_maxima:
            print(f"Nombre: {nombres[i]}, Teléfono: {telefonos[i]}, Email: {mails[i]}, Dirección: {address[i]}, Código Postal: {postalZip[i]}, Región: {region[i]}, País: {country[i]}, Edad: {edades[i]}")

def listar_usuarios_mayor_8000():
    print("Usuarios de México y Brasil con código postal mayor a 8000:")
    for i in range(len(nombres)):
        if postalZip[i] > 8000 and (country[i] == "Mexico" or country[i] == "Brazil"):
            print(f"Nombre: {nombres[i]}, Teléfono: {telefonos[i]}, Email: {mails[i]}, Dirección: {address[i]}, Código Postal: {postalZip[i]}, Región: {region[i]}, País: {country[i]}, Edad: {edades[i]}")

def listar_usuarios_italianos_mayores_40():
    print("Usuarios italianos mayores de 40 años:")
    for i in range(len(nombres)):
        if country[i] == "Italy" and edades[i] > 40:
            print(f"Nombre: {nombres[i]}, Teléfono: {telefonos[i]}, Email: {mails[i]}")

def ordenar_por_nombre(nombre:list)->list:
    for i in range(len(nombre)-1):
        for j in range(i+1 , len(nombre)):
            if nombre[i] > nombre[j]:
                aux_n = nombre[i]
                nombre[i] = nombre[j]
                nombre[j] = aux_n


def listar_datos_mexicanos_por_nombres(nombres:list, telefonos:list, mails:list, address:list, postalZip:list, region:list, country:list, edades:list)->list:
        mexicanos = []
        for i in range(len(country)):
            if country[i] == "Mexico":
                personas_mexicanas = (nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]) 
                mexicanos.append(personas_mexicanas)
        ordenar_por_nombre(mexicanos)
        for mexicano in mexicanos:
            print(f"nombre: {mexicano[0]}, telefonos: {mexicano[1]}, mails: {mexicano[2]}, address: {mexicano[3]}, postalZip: {mexicano[4]}, region: {mexicano[5]}, country: {mexicano[6]}, edades: {mexicano[7]}")

def listar_usuarios_mas_jovenes(nombres, telefonos, mails, address, postalZip, region, country, edades):
    # Crear una lista auxiliar de tuplas con los datos de los usuarios
    usuarios = []
    for i in range(len(nombres)):
        usuario = (nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i])
        usuarios.append(usuario)
    
    # Ordenar la lista de usuarios por edad ascendente y luego por nombre ascendente
    for i in range(len(usuarios)-1):
        for j in range(i+1, len(usuarios)):
            if usuarios[j][7] > usuarios[j][7]:
                usuarios[j], usuarios[j] = usuarios[j], usuarios[j]
            elif usuarios[j][7] == usuarios[j][7] and usuarios[j][0] > usuarios[j][0]:
                usuarios[j], usuarios[j+1] = usuarios[j+1], usuarios[j]
    
    # Imprimir los datos de los usuarios más jóvenes ordenados
    for usuario in usuarios:
        print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Correo: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}, País: {usuario[6]}, Edad: {usuario[7]}")

def listar_usuarios_mexico_brasil_codigo_postal(nombres, telefonos, mails, address, postalZip, region, country, edades):
    # Crear una lista auxiliar de usuarios de México y Brasil con código postal mayor a 8000
    usuarios_mx_br = []
    for i in range(len(nombres)):
        if (country[i] == "Mexico" or country[i] == "Brazil") and postalZip[i] > 8000:
            usuario = (nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i])
            usuarios_mx_br.append(usuario)
    
    # Ordenar la lista de usuarios por nombre y edad de manera descendente
    for i in range(len(usuarios_mx_br)-1):
        for j in range(i + 1, len(usuarios_mx_br)):
            if usuarios_mx_br[i][0] < usuarios_mx_br[j][0]:
                usuarios_mx_br[i], usuarios_mx_br[j] = usuarios_mx_br[j], usuarios_mx_br[i]
            elif usuarios_mx_br[i][0] == usuarios_mx_br[j][0] and usuarios_mx_br[i][7] < usuarios_mx_br[j][7]:
                usuarios_mx_br[i], usuarios_mx_br[j] = usuarios_mx_br[j], usuarios_mx_br[i]
    
    # Imprimir los datos de los usuarios de México y Brasil con código postal mayor a 8000 ordenados
    for usuario in usuarios_mx_br:
        print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Correo: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}, País: {usuario[6]}, Edad: {usuario[7]}")
