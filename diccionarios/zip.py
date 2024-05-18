nombres = ["Ana","Jose","Sol","Beto"]
apellidos = ["Perez","Salas","Gonzalez","Acosta"]
edades = [34,42,26,29]

for e_nombre,e_apellido, e_edad in zip(nombres, apellidos, edades):
    print("Alumno: ", e_nombre, e_apellido, e_edad)