import pygame
import json
import os
from datos import lista  
from constantes import *  

# Inicializar pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("CARRERA UTN")

# Cargar imágenes
imagen_principal = pygame.image.load("utn.png")
imagen_principal = pygame.transform.scale(imagen_principal, (150, 150))
imagen_participante = pygame.image.load("hombre.jpg")
imagen_participante = pygame.transform.scale(imagen_participante, (50, 80))
imagen_llegada = pygame.image.load('utn.png')
imagen_llegada = pygame.transform.scale(imagen_llegada, (80, 80))

# Variables del juego
puntaje = 0
tiempo = 5
indice_pregunta_actual = 0
casilla_actual = 0
juego_comenzado = False
mostrar_puntuaciones = False
pregunta_actual = lista[indice_pregunta_actual]

# Puntuaciones hardcodeadas
puntuaciones_hardcodeadas = [
    {"nombre": "Ana", "puntaje": 150},
    {"nombre": "Luis", "puntaje": 120},
    {"nombre": "Marta", "puntaje": 100},
    {"nombre": "Carlos", "puntaje": 80},
    {"nombre": "Elena", "puntaje": 60},
]

# Leer puntuaciones guardadas
if os.path.exists("puntajes.json"):
    with open("puntajes.json", "r") as archivo:
        puntuaciones_guardadas = [json.loads(linea) for linea in archivo]
else:
    puntuaciones_guardadas = []

# Fuentes
fuente = pygame.font.SysFont("Arial", 24)
fuente_pequena = pygame.font.SysFont("Arial", 10)

# Posiciones de los botones de opciones (dinámicas)
posiciones_opciones = [(195, 101), (369, 101), (539, 101)]

# Bucle principal del juego
corriendo = True
reloj = pygame.time.Clock()

# Posiciones de las casillas (dinámicas)
casillas = [
    (120, 270), (200, 270), (280, 270), (360, 270), (440, 270), (520, 270), (600, 270), (680, 270),
    (120, 370), (200, 370), (280, 370), (360, 370), (440, 370), (520, 370), (600, 370), (680 , 370)
]

# Colores de las casillas
colores_casillas = [
    VERDE, NARANJA, ROJO, AMARILLO, CELESTE, MORADO, VERDE, NARANJA,
    ROJO, AMARILLO, CELESTE, VERDE, NARANJA, VERDE, MORADO, CELESTE 
]

# Textos especiales en las casillas (avanza 1, retrocede 1)
texto_casillas = [
    None, None, None, None, None, None, "avanza 1", None,
    None, None, None, "retrocede 1", None, None, None, None
]

# Rectángulo del participante (inicialmente antes de la primera casilla)
rect_participante = pygame.Rect(40, 250, 80, 100)

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = evento.pos
            if mostrar_puntuaciones:
                if ANCHO // 2 - 75 <= mouse_pos[0] <= ANCHO // 2 + 75 and ALTO - 100 <= mouse_pos[1] <= ALTO - 50:
                    mostrar_puntuaciones = False
            else:
                if 195 <= mouse_pos[0] <= 345 and 478 <= mouse_pos[1] <= 558:  # Botón Comenzar
                    juego_comenzado = True
                    tiempo = 5
                if 408 <= mouse_pos[0] <= 558 and 478 <= mouse_pos[1] <= 558:  # Botón Terminar
                    nombre = input("Ingresa tu nombre: ")
                    datos_jugador = {"nombre": nombre, "puntaje": puntaje}
                    with open("puntajes.json", "a") as archivo:
                        json.dump(datos_jugador, archivo)
                        archivo.write("\n")
                    puntuaciones_guardadas.append(datos_jugador)
                    mostrar_puntuaciones = True  # Mostrar la pantalla de puntuaciones al terminar
                if juego_comenzado:
                    for i, (x, y) in enumerate(posiciones_opciones):
                        if x <= mouse_pos[0] <= x + 150 and y <= mouse_pos[1] <= y + 50:
                            if ['a', 'b', 'c'][i] == pregunta_actual['correcta']:
                                puntaje += 10
                                if casilla_actual < len(casillas) - 1:  # Solo avanzar si no está en la última casilla
                                    casilla_actual += 2  # Avanza 2
                                if casilla_actual >= len(casillas):  # Si llega al final del tablero
                                    casilla_actual = len(casillas)
                            else:
                                casilla_actual -= 1
                                if casilla_actual < 0:
                                    casilla_actual = 0
                            rect_participante.x, rect_participante.y = casillas[casilla_actual]
                            indice_pregunta_actual += 1
                            if indice_pregunta_actual < len(lista):
                                pregunta_actual = lista[indice_pregunta_actual]
                            tiempo = 5
                if 640 <= mouse_pos[0] <= 790 and 10 <= mouse_pos[1] <= 60:  # Botón para mostrar puntuaciones
                    mostrar_puntuaciones = True

    if mostrar_puntuaciones:
        pantalla.fill(AZUL)
        titulo = fuente.render("Puntuaciones", True, BLANCO)
        pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))

        puntuaciones_totales = puntuaciones_hardcodeadas + puntuaciones_guardadas
        puntuaciones_totales = sorted(puntuaciones_totales, key=lambda x: x['puntaje'], reverse=True)[:10]

        for i, puntuacion in enumerate(puntuaciones_totales):
            texto_puntuacion = fuente.render(f"{puntuacion['nombre']}: {puntuacion['puntaje']}", True, BLANCO)
            pantalla.blit(texto_puntuacion, (ANCHO // 2 - texto_puntuacion.get_width() // 2, 80 + i * 40))

        texto_volver = fuente.render("Salir", True, NEGRO)
        pygame.draw.rect(pantalla, CELESTE, (ANCHO // 2 - 75, ALTO - 100, 150, 50))
        pantalla.blit(texto_volver, (ANCHO // 2 - texto_volver.get_width() // 2, ALTO - 90))
    else:
        pantalla.fill(AZUL)
        pantalla.blit(imagen_principal, (5, 10))
        pantalla.blit(imagen_llegada, (20, 350))  # Posición del logo al final del tablero

        # Dibujar casillas
        for i, (x, y) in enumerate(casillas):
            pygame.draw.rect(pantalla, colores_casillas[i], (x, y, 60, 60))
            if texto_casillas[i] is not None:
                texto_especial = fuente_pequena.render(texto_casillas[i], True, BLANCO)
                pantalla.blit(texto_especial, (x + 5, y + 20))

        # Dibujar el participante
        pantalla.blit(imagen_participante, (rect_participante.x, rect_participante.y))

        # Dibuja botones de comenzar y terminar
        pygame.draw.rect(pantalla, CELESTE, (408, 478, 150, 80))
        pygame.draw.rect(pantalla, CELESTE, (195, 478, 150, 80))
        texto_comenzar = fuente.render("Comenzar", True, NEGRO)
        texto_terminar = fuente.render("Terminar", True, NEGRO)
        pantalla.blit(texto_comenzar, (200, 500))
        pantalla.blit(texto_terminar, (420, 500))

        # Mostrar puntaje y tiempo
        texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
        texto_tiempo = fuente.render(f"Tiempo: {tiempo:.0f}", True, BLANCO)
        pantalla.blit(texto_puntaje, (640, 46))
        pantalla.blit(texto_tiempo, (640, 10))

        if juego_comenzado:
            if indice_pregunta_actual < len(lista):
                texto_pregunta = fuente.render(pregunta_actual["pregunta"], True, BLANCO)
                pantalla.blit(texto_pregunta, (195, 10))
                for i, (x, y) in enumerate(posiciones_opciones):
                    pygame.draw.rect(pantalla, CELESTE, (x, y, 150, 50))
                    texto_opcion = fuente.render(pregunta_actual[["a", "b", "c"][i]], True, NEGRO)
                    pantalla.blit(texto_opcion, (x + 5, y + 5))
            else:
                juego_comenzado = False
                mostrar_puntuaciones = True

    # Control del tiempo
    if juego_comenzado:
        tiempo -= reloj.get_time() / 1000
        if tiempo <= 0:
            indice_pregunta_actual += 1
            if indice_pregunta_actual < len(lista):
                pregunta_actual = lista[indice_pregunta_actual]
            tiempo = 5
            casilla_actual -= 1  # Retroceder una casilla si no se responde a tiempo
            if casilla_actual < 0:
                casilla_actual = 0
            rect_participante.x, rect_participante.y = casillas[casilla_actual]

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()