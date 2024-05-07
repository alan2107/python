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
    print("9- Salir")

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