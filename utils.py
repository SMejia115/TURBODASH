'''
The pygame and sys library is imported to manage TurboDash utilities such as image loading, button creation and others, also its system functions, as well as the files needed to execute these tasks.
'''
import pygame
import sys
from button import Button
from menu import Menu
import turbodash as td

'''
The list_buttons() function is the function in charge of creating the buttons and adding them to a list of buttons. It has no input parameters and as output parameters it has the list of buttons.
'''
def list_buttons():
    #Bottons
    tittle_button = Button(50, 170, 500, 100, pygame.image.load("./assets/img/TurboDash.png"), pygame.image.load("./assets/img/TurboDash2.png"), None)
    play_button = Button(100, 300, 200, 50, pygame.image.load("./assets/img/playButton1.png"), pygame.image.load("./assets/img/playButton2.png"), td.run_game)
    quit_button = Button(100, 400, 200, 50, pygame.image.load("./assets/img/exitButton1.png"), pygame.image.load("./assets/img/exitButton2.png"), sys.exit)

    buttons = [tittle_button, play_button, quit_button]
    return buttons

'''
The function menu_load(screen, buttons) is the function in charge of creating the menu. It has screen and buttons as input parameters and as output parameters it has the created menu.
'''
def menu_load(screen, buttons):
    menu = Menu(screen, buttons, pygame.image.load("./assets/img/2.jpg"))
    return menu

'''
The road_image(screen) function is the function responsible for displaying the road. It has no input or output parameters.
'''
def road_image(screen):
    background_image = pygame.image.load('./assets/img/road1.jpg')
    screen.blit(background_image, (0, 0))