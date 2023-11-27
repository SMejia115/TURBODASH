'''
The pygame and sys library for handling events such as cycles, if's or TurboDash screen refresh is imported, as well as the files needed for this task.
'''
import sys
import pygame
import utils
import turbodash as td

'''
The function check_events(car) is the function in charge of checking the different events related to the carriage such as movement. It has cart as input parameter and no output parameters. Depending on the type of event it calls other functions to do the more detailed check.
'''
def check_events(car, settings, screen, bots, pause):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                # Cambiar la bandera de pausa
                return not pause
            elif not pause:
                check_keydown_events(car, event)
        elif event.type == pygame.KEYUP and not pause:
            check_keyup_events(car, event)
        elif event.type == pygame.USEREVENT: # Evento de generación de bots (CADA CIERTO TIEMPO)
            utils.generate_bot(settings, screen, bots)
        elif event.type == pygame.USEREVENT+1: # Evento de aumentar la velocidad de los bots (CADA CIERTO TIEMPO) y la generación de bots   
            settings.bg_speed *= 1.5
            settings.bot_generation_time *= 1.5

    return pause


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
        td.main_menu()

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
def refresh_screen(screen, car, settings, bg_y, current_bg_index, next_bg_index, bots):
    bg_y, current_bg_index, next_bg_index = utils.update_background(settings, screen, bg_y, current_bg_index, next_bg_index)
    car.draw()
    utils.update_bots(bots, settings, car, screen)
    utils.draw_bots(bots)
    pygame.display.flip()
    return bg_y, current_bg_index, next_bg_index

