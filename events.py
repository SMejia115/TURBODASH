import sys
import pygame
import utils

def check_events(car):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(car, event)

        elif event.type == pygame.KEYUP:
            check_keyup_events(car, event)

def check_keydown_events(car, event):
    if event.key == pygame.K_RIGHT:
        car.moving_right = True

    elif event.key == pygame.K_LEFT:
        car.moving_left = True

    elif event.key == pygame.K_UP:
        car.moving_up = True

    elif event.key == pygame.K_DOWN:
        car.moving_down = True

    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(car, event):
    if event.key == pygame.K_RIGHT:
        car.moving_right = False

    elif event.key == pygame.K_LEFT:
        car.moving_left = False

    elif event.key == pygame.K_UP:
        car.moving_up = False
        
    elif event.key == pygame.K_DOWN:
        car.moving_down = False

def refresh_screen(screen, car):
    utils.road_image(screen)
    car.blitme()
    pygame.display.flip()