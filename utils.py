import pygame
import sys
from button import Button
from menu import Menu
import turbodash as td

def list_buttons():

    #Bottons
    tittle_button = Button(50, 170, 500, 100, pygame.image.load("./assets/img/TurboDash.png"), pygame.image.load("./assets/img/TurboDash2.png"), None)
    play_button = Button(100, 300, 200, 50, pygame.image.load("./assets/img/playButton1.png"), pygame.image.load("./assets/img/playButton2.png"), td.run_game)
    quit_button = Button(100, 400, 200, 50, pygame.image.load("./assets/img/exitButton1.png"), pygame.image.load("./assets/img/exitButton2.png"), sys.exit)

    buttons = [tittle_button, play_button, quit_button]
    return buttons

def menu_load(screen, buttons):
    menu = Menu(screen, buttons, pygame.image.load("./assets/img/2.jpg"))
    return menu