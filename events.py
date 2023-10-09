'''
The pygame and sys library for handling events such as cycles, if's or TurboDash screen refresh is imported, as well as the files needed for this task.
'''
import sys
import pygame
import utils

'''
The function check_events(car) is the function in charge of checking the different events related to the carriage such as movement. It has cart as input parameter and no output parameters. Depending on the type of event it calls other functions to do the more detailed check.
'''
def check_events(car):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(car, event)

        elif event.type == pygame.KEYUP:
            check_keyup_events(car, event)

'''
The function check_keydown_events(car, events) is in charge of checking the different events related to the keydown of the keys. It has as input parameters the car and the event to analyze and has no output parameters. Depending on the type of event it returns True boolean values of car movement.
'''
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

'''
The function check_keyup_events(car, events) is in charge of checking the different events related to the keyup of the keys. It has as input parameters the car and the event to analyze and has no output parameters. Depending on the type of event it returns False boolean values of car movement.
'''
def check_keyup_events(car, event):
    if event.key == pygame.K_RIGHT:
        car.moving_right = False

    elif event.key == pygame.K_LEFT:
        car.moving_left = False

    elif event.key == pygame.K_UP:
        car.moving_up = False
        
    elif event.key == pygame.K_DOWN:
        car.moving_down = False

'''
The function refresh_screen(screen, car) is in charge of refreshing the screen for the different elements that interact in the game such as the car or the road. It has as input parameters the screen and the car and no output parameters. It calls the different functions and class methods needed for this task.
'''
def refresh_screen(screen, car):
    utils.road_image(screen)
    car.draw()
    pygame.display.flip()