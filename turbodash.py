import pygame
import sys

from button import Button




title_image = pygame.image.load('./images/TurboDash.png')
title_hover_image = pygame.image.load('./images/TurboDash2.png')

play_button_image = pygame.image.load('./images/playButton1.png')
play_button_hover_image = pygame.image.load('./images/playButton2.png')
menu_button_image = pygame.image.load('./images/menuButton1.png')
menu_button_hover_image = pygame.image.load('./images/menuButton2.png')
exit_button_image = pygame.image.load('./images/exitButton1.png')
exit_button_hover_image = pygame.image.load('./images/exitButton2.png')


def prueba_funcion():
    print('¡Funciona!')


def start_game():
    pygame.quit()  # Cerrar la ventana del menú
    play_turboDash()



def play_turboDash():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('TurboDash')

    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False


        pygame.display.update()

    pygame.quit()






def main_menu():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption('Main Menu')
    
    title_button = Button(240, 100, 600, 100, title_image, title_hover_image, prueba_funcion)
    play_button = Button(320, 270, 150, 50, play_button_image, play_button_hover_image, play_turboDash)
    options_button = Button(320, 330, 150, 50, menu_button_image, menu_button_hover_image, prueba_funcion)
    exit_button = Button(320, 390, 150, 50, exit_button_image, exit_button_hover_image, prueba_funcion)
    

    run_menu = True

    while run_menu:
        mouse_pos = pygame.mouse.get_pos()

        buttons = [play_button, options_button, exit_button, title_button]

        
# En el bucle de eventos:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
            elif event.type == pygame.MOUSEMOTION:
                for button in buttons:
                    button.check_hover(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in buttons:
                        if button.is_hovered:
                            button.perform_action()

        screen.fill((18, 40, 53))
        
        background_image = pygame.image.load('./images/background.png')
        screen.blit(background_image, (0, 0))

        for button in buttons:
            button.draw(screen)
        
        # else:
        #     screen.blit(play_button.hover_image, play_button.rect)

        

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main_menu()
