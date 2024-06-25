import pygame
import sys
from datos import lista

# Inicializar pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Carrera de Mentes")

# Cargar imagen
imagen_principal = pygame.image.load("logomentes.png")
imagen_principal = pygame.transform.scale(imagen_principal, (200, 200))

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)
AZUL = (10, 73, 123)
AMARILLO = (255, 255, 0)

# Variables globales del juego
puntaje = 0
indice_pregunta_actual = 0
intentos = 0

# Fuentes
fuente = pygame.font.SysFont("Arial", 24)
texto_pregunta = fuente.render("PREGUNTA", True, GRIS)
texto_reiniciar = fuente.render("REINICIAR", True, GRIS)

# Posiciones de los botones de opciones
posiciones_opciones = [(20, 350), (250, 350), (500, 350)]

# Bucle principal del juego
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = evento.pos
            if indice_pregunta_actual < len(lista):
                # Verificar si se hizo clic en alguna de las opciones
                for i, (x, y) in enumerate(posiciones_opciones):
                    if x <= posicion_click[0] <= x + 760 and y <= posicion_click[1] <= y + 40:
                        opcion_seleccionada = ['a', 'b', 'c'][i]
                        opcion_correcta = lista[indice_pregunta_actual]['correcta']
                        if opcion_seleccionada == opcion_correcta:
                            puntaje += 10
                            indice_pregunta_actual += 1
                            intentos = 0
                        else:
                            intentos += 1
                            if intentos >= 2:
                                indice_pregunta_actual += 1
                                intentos = 0

            # Verificar si se hizo clic en el botón de reiniciar
            if 350 <= posicion_click[0] <= 550 and 30 <= posicion_click[1] <= 130:
                puntaje = 0
                indice_pregunta_actual = 0
                intentos = 0

    pantalla.fill(AZUL)
    pantalla.blit(imagen_principal, (5, 10))
    pygame.draw.rect(pantalla, AMARILLO, (300, 20, 180, 80))
    pygame.draw.rect(pantalla, AMARILLO, (300, 500, 180, 80))
    pantalla.blit(texto_pregunta,(320, 45))
    pantalla.blit(texto_reiniciar,(330,530))


    if indice_pregunta_actual >= len(lista):
        texto_superficie = fuente.render("No hay más preguntas.", True, NEGRO)
        pantalla.blit(texto_superficie, (20, 100))
    else:
        datos_pregunta = lista[indice_pregunta_actual]
        texto_superficie = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
        pantalla.blit(texto_superficie, (300, 150))

        texto_superficie = fuente.render(f"Tema: {datos_pregunta['tema']}", True, AMARILLO)
        pantalla.blit(texto_superficie, (20, 220))

        texto_superficie = fuente.render(datos_pregunta['pregunta'], True, BLANCO)
        pantalla.blit(texto_superficie, (20, 250))

        for i, opcion in enumerate(['a', 'b', 'c']):
            texto_opcion = fuente.render(datos_pregunta[opcion], True, AMARILLO)
            pantalla.blit(texto_opcion, posiciones_opciones[i])

    pygame.display.update()