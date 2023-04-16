import pygame
import random

# inicializar Pygame
pygame.init()

# definir colores
white = (255, 255, 255)
black = (0, 0, 0)

# definir dimensiones de pantalla
width = 800
height = 600


# crear pantalla
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Esquivando Sandías")

# cargar imágenes
ship_img = pygame.image.load("nave.png")
watermelon_img = pygame.image.load("sandia.png")

# definir posición inicial de la nave
ship_x = width // 2 - ship_img.get_width() // 2
ship_y = height - 50

# definir posición y velocidad inicial de la sandía
watermelon_x = random.randint(0, width - watermelon_img.get_width())
watermelon_y = 0
watermelon_speed = 5

# definir puntuación inicial
score = 0

# definir fuente para el texto
font = pygame.font.SysFont(None, 30)

# definir bandera para controlar el juego
game_over = False

# crear reloj para controlar la velocidad de fotogramas
clock = pygame.time.Clock()

# bucle principal del juego
while not game_over:
    # manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_x -= 10
            elif event.key == pygame.K_RIGHT:
                ship_x += 10
            elif event.key == pygame.K_UP:
                ship_y -= 10
            elif event.key == pygame.K_DOWN:
                ship_y += 10

    # mover la sandía hacia abajo
    watermelon_y += watermelon_speed

    # si la sandía llega al fondo de la pantalla, reubicarla aleatoriamente en la parte superior
    if watermelon_y > height:
        watermelon_x = random.randint(0, width - watermelon_img.get_width())
        watermelon_y = 0
        score += 1
        watermelon_speed += 1

    # dibujar la nave y la sandía
    screen.fill(white)
    screen.blit(ship_img, (ship_x, ship_y))
    screen.blit(watermelon_img, (watermelon_x, watermelon_y))

    # dibujar la puntuación
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))

    # detectar colisiones entre la nave y la sandía
    if ship_x < watermelon_x + watermelon_img.get_width() and ship_x + ship_img.get_width() > watermelon_x and ship_y < watermelon_y + watermelon_img.get_height() and ship_y + ship_img.get_height() > watermelon_y:
        game_over = True

    # mover la nave con las flechas izquierda y derecha
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship_x > 0:
        ship_x -= 5
    if keys[pygame.K_RIGHT] and ship_x < width - ship_img.get_width():
        ship_x += 5

    # mover la nave con las flechas arriba y abajo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ship_y > 0:
        ship_y -= 5
    if keys[pygame.K_DOWN] and ship_y < width - ship_img.get_width():
        ship_y += 5    

    # dibujar texto de Game Over
    if game_over:
        game_over_text = font.render("Game Over - Presiona enter para salir", True, black)
        screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))

        # esperar a que el usuario presione Enter
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
                        quit()

            pygame.display.update()
            clock.tick(60)

    # actualizar la pantalla
    pygame.display.update()

    # controlar la velocidad de fotogramas
    clock.tick(60)

# salir de Pygame
pygame.quit()
quit()
