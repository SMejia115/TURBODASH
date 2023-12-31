'''
TurboDash was created by Brayan Cataño Giraldo and Santiago Mejia Orejuela in 2023.
'''

'''
The pygame and sys library for handling events such as cycles, if's or TurboDash screen refresh 
is imported, as well as the files needed for this task.
'''
import sys
import pygame
import utils
import turbodash as td
from stats import Stats
import math
from settings import Settings

'''
The settings class is initialized.
'''
settings = Settings()

'''
The pygame.mixer library is imported to play the background music of the game.
'''
pygame.mixer.init()

'''
The function check_events(car) is the function in charge of checking the different events related to the carriage such as movement. It has cart as input parameter and no output parameters. Depending on the type of event it calls other functions to do the more detailed check.

Function name: check_events
Input: car
Output: None
description: This function is used to check the different events related to the carriage such as movement.

'''
def check_events(car, settings, screen, bots, pause, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                # Change the pause flag when pressing p
                return not pause
            elif not pause:
                check_keydown_events(car, event, settings, screen, stats)
        elif event.type == pygame.KEYUP and not pause:
            check_keyup_events(car, event, stats)
        elif event.type == pygame.USEREVENT: # Evento de generación de bots (CADA CIERTO TIEMPO)
            utils.generate_bot(settings, screen, bots)
        elif event.type == pygame.USEREVENT+1: # Event to increase the speed of bots and bot generation.   
            settings.bg_speed *= 1.1
            settings.bot_generation_time *= 0.9
            # print("Bots speed increased =", settings.bg_speed, "Bots generation time decreased =", settings.bot_generation_time)
        elif event.type == pygame.USEREVENT+2: # Event to increase the score
            # stats.score += 1
            stats.update_stats(math.floor(settings.bg_speed))
            # stats.draw_score(screen)
    return pause


'''
The function check_keydown_events(car, events) is in charge of checking the different events 
related to the keydown of the keys. It has as input parameters the car and the event to analyze and 
has no output parameters. Depending on the type of event it returns True boolean values of car movement.

Function name: check_keydown_events
Input: car, event
Output: None
description: This function is used to check the different events related to the keydown of the keys.

'''
def check_keydown_events(car, event, settings, screen, stats):
    if event.key == pygame.K_RIGHT:
        car.moving_right = True
        pygame.mixer.Sound.play(settings.car)

    elif event.key == pygame.K_LEFT:
        car.moving_left = True
        pygame.mixer.Sound.play(settings.car)

    elif event.key == pygame.K_UP:
        car.moving_up = True
        pygame.mixer.Sound.play(settings.car)

    elif event.key == pygame.K_DOWN:
        car.moving_down = True
        pygame.mixer.Sound.play(settings.car)

    elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
        pygame.mixer.Sound.play(settings.horn)

    elif event.key == pygame.K_q:
        td.main_menu()
    
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

    elif event.key == pygame.K_SPACE:
        stats.activate_power()
            
            

'''
The function check_keyup_events(car, events) is in charge of checking the different events 
related to the keyup of the keys. It has as input parameters the car and the event to analyze and has 
no output parameters. Depending on the type of event it returns False boolean values of car movement.

Function name: check_keyup_events
Input: car, event
Output: None
description: This function is used to check the different events related to the keyup of the keys.

'''
def check_keyup_events(car, event, stats):
    if event.key == pygame.K_RIGHT:
        car.moving_right = False

    elif event.key == pygame.K_LEFT:
        car.moving_left = False

    elif event.key == pygame.K_UP:
        car.moving_up = False
        
    elif event.key == pygame.K_DOWN:
        car.moving_down = False

    # elif event.key == pygame.K_SPACE:
    #     stats.power_up = False


'''
The function refresh_screen(screen, car) is in charge of refreshing the screen for the different
elements that interact in the game such as the car or the road. It has as input parameters the screen 
and the car and no output parameters. It calls the different functions and class methods needed for this task.

Function name: refresh_screen
Input: screen, car
Output: None
description: This function is used to refresh the screen for the different elements that interact in the game such as the car or the road.
'''
def refresh_screen(screen, car, settings, bg_y, current_bg_index, next_bg_index, bots, stats):

    bg_y, current_bg_index, next_bg_index = utils.update_background(settings, screen, bg_y, current_bg_index, next_bg_index)
    car.draw()
    utils.update_bots(bots, settings, car, screen, stats)
    utils.draw_bots(bots)

    stats.draw_score(screen)
    stats.draw_power_quantity(screen)

    pygame.display.flip()
    return bg_y, current_bg_index, next_bg_index

