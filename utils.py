import pygame
import sys
from button import Button
from menu import Menu

def list_buttons():

    #Bottons
    play_button = Button(300, 200, 200, 50, pygame.image.load("./assets/img/playButton1.png"), pygame.image.load("./assets/img/playButton2.png"), None)
    quit_button = Button(300, 300, 200, 50, pygame.image.load("./assets/img/exitButton1.png"), pygame.image.load("./assets/img/exitButton2.png"), sys.exit)

    buttons = [play_button, quit_button]
    return buttons

def menu_load(screen, buttons):
    menu = Menu(screen, buttons, pygame.image.load("./assets/img/background.png"))
    return menu