'''
The pygame and sys library is imported to manage the TurboDash game and its system functions, as well as the files needed to run the game base.
'''
import pygame 
import sys
from settings import Settings
import utils
from car import Car
import events
 

'''
The main_manu() function is the main function and is the one called when the game is started. It has no input or output parameters. It initializes pygame, the screen with its dimensions and settings and the main menu of the game.
'''
def main_menu():
  pygame.init()
  settings = Settings()
  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
  pygame.display.set_caption("TurboDash")
  
  buttons_menu, buttons_pause = utils.list_buttons()

  menu = utils.menu_load(screen, buttons_menu)
  menu.run()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    pygame.display.flip()

'''
The run_game() function is the one that starts the game and is called after pressing the play button. It has no input or output parameters. It initializes the cart and calls the functions and classes in charge of the car and screen refresh functions.
'''
def run_game():
  pygame.init()
  settings = Settings()
  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
  pygame.display.set_caption("TurboDash")

  car = Car(settings, screen, utils.car_image())

  while True:
      events.check_events(car)
      car.update(settings)
      events.refresh_screen(screen, car)

'''
If startup to call the main_menu() function.
'''
if __name__ == "__main__":
    main_menu()