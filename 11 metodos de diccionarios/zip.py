nombres = ["Ana","Jose","Sol","Beto"]
apellidos = ["Perez","Salas","Gonzalez","Acosta"]
edades = [34,42,26,29]

'''
toma
como argumento dos o más objetos iterables (idealmente
cada uno de ellos con la misma cantidad de elementos) y
retorna un nuevo iterable cuyos elementos son tuplas que
contienen un elemento de cada uno de los iteradores
originales en la misma posición.
'''

for e_nombre,e_apellido, e_edad in zip(nombres, apellidos, edades):
    print("Alumno: ", e_nombre, e_apellido, e_edad)