import pygame
import random
import math

# Inicializamos Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título e ícono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("space-ship.png")
pygame.display.set_icon(icono)

# Fondo
fondo = pygame.image.load("Fondo.jpg")

# Jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 370
jugador_y = 480
jugador_x_cambio = 0

# Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
num_enemigos = 6

for i in range(num_enemigos):
    img_enemigo.append(pygame.image.load("enemigo64.png"))
    enemigo_x.append(random.randint(0, 735))
    enemigo_y.append(random.randint(50, 150))
    enemigo_x_cambio.append(4)
    enemigo_y_cambio.append(40)

# Bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 480
bala_y_cambio = 10
bala_visible = False

# Puntuación
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# Fuente para "Game Over"
fuente_final = pygame.font.Font('freesansbold.ttf', 64)


# Función para mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Función para mostrar "Game Over"
def game_over():
    texto_final = fuente_final.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(texto_final, (200, 250))

    # Mostrar el puntaje final
    texto_puntaje_final = fuente.render(f"Puntaje final: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto_puntaje_final, (250, 350))


# Función del jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Función del enemigo
def enemigo(x, y, i):
    pantalla.blit(img_enemigo[i], (x, y))


# Disparo de bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Detectar colisión
def hay_colision(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Bucle principal del juego
ejecutando = True
game_over_estado = False  # Variable para indicar si el juego ha terminado

while ejecutando:

    # Fondo de pantalla
    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        # Movimiento del jugador
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -5
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 5
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Actualizar la posición del jugador
    jugador_x += jugador_x_cambio

    # Mantener al jugador dentro de los límites de la pantalla
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Movimiento del enemigo
    for i in range(num_enemigos):

        # Verificar si el juego ha terminado (colisión con el jugador)
        if enemigo_y[i] > 440:
            for j in range(num_enemigos):
                enemigo_y[j] = 2000  # Mueve a todos los enemigos fuera de la pantalla
            game_over_estado = True
            break

        enemigo_x[i] += enemigo_x_cambio[i]
        if enemigo_x[i] <= 0:
            enemigo_x_cambio[i] = 4
            enemigo_y[i] += enemigo_y_cambio[i]
        elif enemigo_x[i] >= 736:
            enemigo_x_cambio[i] = -4
            enemigo_y[i] += enemigo_y_cambio[i]

        # Colisión entre la bala y el enemigo
        colision = hay_colision(enemigo_x[i], enemigo_y[i], bala_x, bala_y)
        if colision:
            bala_y = 480
            bala_visible = False
            puntaje += 1
            enemigo_x[i] = random.randint(0, 735)
            enemigo_y[i] = random.randint(50, 150)

        enemigo(enemigo_x[i], enemigo_y[i], i)

    # Movimiento de la bala
    if bala_y <= 0:
        bala_y = 480
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # Dibujar jugador y enemigos si el juego no ha terminado
    if not game_over_estado:
        jugador(jugador_x, jugador_y)
        mostrar_puntaje(texto_x, texto_y)
    else:
        game_over()  # Mostrar "Game Over" si el juego ha terminado

    pygame.display.update()
