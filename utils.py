'''
The pygame and sys library is imported to manage TurboDash utilities such as image loading, button creation and others, also its system functions, as well as the files needed to execute these tasks.
'''
import pygame
import sys
from button import Button
from menu import Menu
import turbodash as td
from settings import Settings

settings = Settings()
'''
The list_buttons() function is the function in charge of creating the buttons and adding them to a list of buttons. It has no input parameters and as output parameters it has the list of buttons.
'''
def list_buttons():
    #Bottons menu start
    tittle_button = Button(50, 50, 500, 100, pygame.image.load("./assets/img/logo/TurboDash.png"), pygame.image.load("./assets/img/logo/TurboDash2.png"), None)
    play_button = Button(330, 300, 200, 50, pygame.image.load("./assets/img/buttons/playButton1.png"), pygame.image.load("./assets/img/buttons/playButton2.png"), td.run_game)
    quit_button = Button(330, 400, 200, 50, pygame.image.load("./assets/img/buttons/exitButton1.png"), pygame.image.load("./assets/img/buttons/exitButton2.png"), sys.exit)
    buttons_start = [tittle_button, play_button, quit_button]

    #Bottons menu pause
    pause_button = Button(550, 50, 200, 50, pygame.image.load("./assets/img/logo/Pause.png"), pygame.image.load("./assets/img/logo/Pause2.png"), None)
    buttons_pause = [tittle_button, play_button, quit_button, pause_button]

    return buttons_start, buttons_pause

'''
The function menu_load(screen, buttons) is the function in charge of creating the menu. It has screen and buttons as input parameters and as output parameters it has the created menu.
'''
def menu_load(screen, buttons):
    menu = Menu(screen, buttons, pygame.image.load("./assets/img/backgrounds/2.jpg"))
    return menu

def pause_load(screen, buttons):
    pause = Menu(screen, buttons, pygame.image.load("./assets/img/backgrounds/1.jpg"))
    return pause

'''
The road_image(screen) function is the function responsible for displaying the road. It has no input or output parameters.
'''
def road_image(screen):
    background_image = pygame.image.load('./assets/img/roads/road1.jpg')
    screen.blit(background_image, (0, 0))

'''
The car_image() function is the function responsible for loading the image of the car and giving it transparency
'''
def car_image():
    car = pygame.image.load("./assets/img/cars/Audi.png").convert()
    car.set_colorkey(settings.car_colorkey)
    return car