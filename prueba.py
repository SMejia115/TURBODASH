import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 910
screen_height = 700

# Crear la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))

# Lista de imágenes de fondo
background_images = [pygame.image.load('./assets/img/roads/snowRoad1.png'),
                     pygame.image.load('./assets/img/roads/snowRoad2.png'),
                     pygame.image.load('./assets/img/roads/forestRoad2.png'),
                     pygame.image.load('./assets/img/roads/forestRoad1.png')]

# Coordenada inicial para el fondo
bg_y = 0

# Velocidad del carro y del fondo
car_speed = 2
bg_speed = 2

# Coordenadas iniciales del carro
car_x = screen_width // 2
car_y = screen_height - 100
car_image = pygame.image.load('./assets/img/cars/car1.png')

# Índice de la imagen actual y próxima
current_bg_index = 0
next_bg_index = random.randint(0, len(background_images) - 1)

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x - car_speed > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x + car_speed < screen_width - 64:
        car_x += car_speed
    if keys[pygame.K_UP] and car_y - car_speed > 0:
        car_y -= car_speed
    if keys[pygame.K_DOWN] and car_y + car_speed < screen_height - 64:
        car_y += car_speed

    # Mover el fondo en dirección opuesta al movimiento del carro
    bg_y += bg_speed

    # Si el fondo se desplaza fuera de la pantalla, reiniciarlo
    if bg_y >= screen_height:
        # Cambiar la imagen actual a la siguiente
        current_bg_index = next_bg_index
        # Seleccionar una nueva imagen para próxima
        next_bg_index = random.randint(0, len(background_images) - 1)
        # Reiniciar la posición del fondo
        bg_y = 0

    # Dibujar el fondo en la pantalla
    screen.blit(background_images[current_bg_index], (0, bg_y))
    screen.blit(background_images[next_bg_index], (0, bg_y - screen_height))

    # Dibujar el carro en su posición actual
    screen.blit(car_image, (car_x, car_y))

    # Actualizar la pantalla
    pygame.display.update()
