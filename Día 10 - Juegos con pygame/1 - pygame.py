import pygame
import random
import math

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de ovnis")
icono = pygame.image.load('space-ship.png')
pygame.display.set_icon(icono)

fondo = pygame.image.load("Fondo.jpg")

# puntaje
puntaje = 0

# Variables del jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 500
jugador_cambio_x = 0
jugador_cambio_y = 0

# Variables de enemigo
img_enemigo = pygame.image.load("enemigo64.png")
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_cambio_x = 3
enemigo_cambio_y = 50


# Variables de la bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_cambio_x = 0
bala_cambio_y = 3
bala_visible = False


"""
La función blit() en Pygame se utiliza para dibujar o renderizar una superficie (surface), 
como una imagen, sobre otra superficie, que normalmente es la pantalla del juego.
"""


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))


def dispara_bala(x, y):
    global  bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


def detectar_colision(x_1, y_1, x_2, y_2):
    primer_valor_al_cuadrado = math.pow(x_2 - x_1, 2)
    segundo_valor_al_cuadrado = math.pow(y_2 - y_1, 2)
    distancia = math.sqrt(primer_valor_al_cuadrado + segundo_valor_al_cuadrado)
    if distancia < 27:
        return True
    else:
        return False


en_ejecucion = True

while en_ejecucion:
    # RGB
    # pantalla.fill((205, 144, 228))
    # Fondo de pantalla
    pantalla.blit(fondo, (0,0))

    for evento in pygame.event.get():
        # Evento que se ejcuta cuando se cierra la ventana
        if evento.type == pygame.QUIT:
            en_ejecucion = False

        # Evento cuando se presiona una tecla
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                # Movemos al jugador
                jugador_cambio_x = -5
            if evento.key == pygame.K_RIGHT:
                jugador_cambio_x = 5
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    dispara_bala(bala_x, bala_y)

        # Evento que se captura cuando se suelta una tecla
        if evento.type == pygame.KEYUP:
            # Detenemos el movimiento del jugador
            jugador_cambio_x = 0

    # Actualiza el movimiento del jugador
    jugador_x += jugador_cambio_x
    # Mantiene al jugador dentro de los límites
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Actualiza el movimiento del enemigo
    enemigo_x += enemigo_cambio_x
    # Mantiene al enemigo dentro de los límites
    if enemigo_x <= 0:
        enemigo_cambio_x = 3
        enemigo_y += enemigo_cambio_y
    elif enemigo_x >= 736:
        enemigo_cambio_x = -3
        enemigo_y += enemigo_cambio_y

    # Movimiento de la bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        dispara_bala(bala_x, bala_y)
        bala_y -= bala_cambio_y

    # Colisión
    colision = detectar_colision(enemigo_x, enemigo_y, bala_x, bala_y)
    if colision:
        bala_y = 500
        bala_visible = False
        puntaje += 1
        enemigo_x = random.randint(0, 736)
        enemigo_y = random.randint(50, 200)

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)
    pygame.display.update()
