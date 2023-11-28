'''
The pygame and sys library is imported to manage TurboDash utilities such as image loading, button creation and others, also its system functions, as well as the files needed to execute these tasks.
'''
import pygame
import sys
from button import Button
from menu import Menu
import turbodash as td
from settings import Settings
from pygame.sprite import Group
from botVehicle import BotVehicle
import random


settings = Settings()

'''
The list_buttons() function is the function in charge of creating the buttons and adding them to a list of buttons. It has no input parameters and as output parameters it has the list of buttons.
'''
def list_buttons():
    settings = Settings()
    #Bottons menu start
    tittle_start_button = Button(250, 100, 500, 100, pygame.image.load("./assets/img/logo/Td.png"), pygame.image.load("./assets/img/logo/Td.png"), None)
    play_start_button = Button(380, 300, 150, 50, pygame.image.load("./assets/img/buttons/play1.png"), pygame.image.load("./assets/img/buttons/play2.png"), td.run_game)
    info_start_button = Button(380, 370, 150, 50, pygame.image.load("./assets/img/buttons/settings1.png"), pygame.image.load("./assets/img/buttons/settings2.png"), td.info_game)
    quit_start_button = Button(380, 440, 150, 50, pygame.image.load("./assets/img/buttons/exit1.png"), pygame.image.load("./assets/img/buttons/exit2.png"), sys.exit)
    buttons_start = [tittle_start_button, info_start_button, play_start_button, quit_start_button]

    #Bottons menu pause
    pause_button = Button(0, 0, 910, 700, pygame.image.load("./assets/img/backgrounds/pause.png"), pygame.image.load("./assets/img/backgrounds/pause.png"), None)
    buttons_pause = [pause_button]

    #Bottons menu lost
    lost_button = Button(0, 0, 910, 700, pygame.image.load("./assets/img/backgrounds/lost.png"), pygame.image.load("./assets/img/backgrounds/lost.png"), None)
    buttons_lost = [lost_button]

    #Bottons menu credits
    credits_button = Button(0, 0, 910, 700, pygame.image.load("./assets/img/backgrounds/credits.png"), pygame.image.load("./assets/img/backgrounds/credits.png"), None)
    back_credits_button = Button(380, 620, 150, 50, pygame.image.load("./assets/img/buttons/back1.png"), pygame.image.load("./assets/img/buttons/back2.png"), td.main_menu)
    buttons_credits = [credits_button, back_credits_button]

    return buttons_start, buttons_pause, buttons_credits, buttons_lost

    
'''
The function menu_load(screen, buttons) is the function in charge of creating the menu. It has screen and buttons as input parameters and as output parameters it has the created menu.
'''
def menu_load(screen, buttons):
    menu = Menu(screen, buttons, pygame.image.load("./assets/img/roads/forestRoad1.png"))
    return menu

def pause_load(screen, buttons):
    pause = Menu(screen, buttons, pygame.image.load("./assets/img/backgrounds/1.jpg"))
    return pause

'''
The road_image(screen) function is the function responsible for displaying the road. It has no input or output parameters.
'''
def road_image(screen, settings):
    bg_y = 0
    current_bg_index = 0
    next_bg_index = random.randint(0, len(settings.background_images) - 1)

    bg_y, current_bg_index, next_bg_index = update_background(settings, screen, bg_y, current_bg_index, next_bg_index)

    # background_image = pygame.image.load('./assets/img/roads/forestRoad1.png')
    # screen.blit(background_image, (0, 0))

'''
The car_image() function is the function responsible for loading the image of the car and giving it transparency
'''
def car_image():
    car = pygame.image.load("./assets/img/cars/car2.png")
    # .convert()
    # car.set_colorkey(settings.car_colorkey)
    return car

'''
Function update_background(settings, screen) is the function in charge of updating the background image. It has screen and settings as input parameters and as output parameters it has the updated background image.
'''


def update_background(settings, screen, bg_y, current_bg_index, next_bg_index):
    bg_y += settings.bg_speed
    # Si el fondo se desplaza fuera de la pantalla, reiniciarlo
    if bg_y >= settings.screen_height:
        # Cambiar la imagen actual a la siguiente
        current_bg_index = next_bg_index
        # Seleccionar una nueva imagen para próxima
        next_bg_index = random.randint(0, len(settings.background_images) - 1)
        # Reiniciar la posición del fondo
        bg_y = 0

    # Dibujar el fondo en la pantalla
    screen.blit(settings.background_images[current_bg_index], (0, bg_y))
    screen.blit(settings.background_images[next_bg_index], (0, bg_y - settings.screen_height))
    return bg_y, current_bg_index, next_bg_index


'''
Function generateBots(screen, settings, bot_image) is the function in charge of generating the bots. It has screen, settings and bot_image as input parameters and as output parameters it has the generated bots.
'''

def generate_bot(settings, screen, bots):
    bot_image = random.choice(settings.bot_images)
    rail = random.randint(0, 3)
    if (rail == 0 or rail == 1):
        direction = 1
    elif (rail == 2 or rail == 3):
        direction = -1
    bot = BotVehicle(settings, screen, bot_image, direction, rail)
    bots.add(bot)
    bot.draw()
    # print("Bot generated , rail: ", rail, " direction: ", direction)


def update_bots(bots, settings, car, screen, stats):
    for bot in bots.copy():
        bot.update(settings)
        if bot.rect.top >= settings.screen_height:
            bots.remove(bot)
            # print("Bot deleted")
    colision = check_collisions(car, bots)
    if colision:
        bots.empty()
        settings.bg_speed = 5
        settings.bot_generation_time = 10000
        # print("Bots deleted")
        stats.reset_score()
        td.lost_menu(screen)
        return True

def draw_bots(bots):
    for bot in bots.sprites():
        bot.draw()

def check_collisions(car, bots):
    if pygame.sprite.spritecollideany(car, bots):
        # print("Car crashed")
        return True
    return False