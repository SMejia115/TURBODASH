'''
The pygame and sys library is imported to manage the TurboDash game and its system functions, as well as the files needed to run the game base.
'''
import pygame 
import sys
from settings import Settings
import utils
from car import Car
import events 
import random
from botVehicle import BotVehicle
from pygame.sprite import Group
from stats import Stats

'''
The main_manu() function is the main function and is the one called when the game is started. It has no input or output parameters. It initializes pygame, the screen with its dimensions and settings and the main menu of the game.
'''
settings = Settings()
stats = Stats(settings)
songs = settings.music

def main_menu():
  pygame.init()
  pygame.mixer.init()
  settings = Settings()
  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
  pygame.display.set_caption("¡Welcome to Turbodash!")
  
  buttons_menu, buttons_pause, buttons_credits, buttons_lost = utils.list_buttons()

  menu = utils.menu_load(screen, buttons_menu)
  menu.run()

  # while True:
  #   for event in pygame.event.get():
  #     if event.type == pygame.QUIT:
  #       sys.exit()
  #   pygame.display.flip()

'''
The run_game() function is the one that starts the game and is called after pressing the play button. It has no input or output parameters. It initializes the cart and calls the functions and classes in charge of the car and screen refresh functions.
'''
def run_game(image_car):
  # pygame.init()
  settings = Settings()
  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
  pygame.display.set_caption("TurboDash")
  car = Car(settings, screen, image_car)
  bots = Group()

  # stats = Stats(settings)

  #Initial background configuration

  bg_y = 0
  current_bg_index = 0
  next_bg_index = random.randint(0, len(settings.background_images) - 1)

  clock = pygame.time.Clock()

  pygame.time.set_timer(pygame.USEREVENT, settings.bot_generation_time)
  pygame.time.set_timer(pygame.USEREVENT+1, 10000)
  pygame.time.set_timer(pygame.USEREVENT+2, 200)
  pause = False
	
  while True:
    pause = events.check_events(car, settings, screen, bots, pause, stats)
    if not pygame.mixer.music.get_busy():
        play_music()
    if pause:
      pause = pause_menu(screen, pause)
    if not pause:
        car.update(settings)
        bg_y, current_bg_index, next_bg_index = events.refresh_screen(screen, car, settings, bg_y, current_bg_index, next_bg_index, bots, stats)


'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

def info_game():
  # pygame.init()
  settings = Settings()
  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
  pygame.display.set_caption("¡Credits TurboDash!")

  buttons_menu, buttons_pause, buttons_credits, buttons_lost = utils.list_buttons()

  menu = utils.menu_load(screen, buttons_credits)
  menu.run()

  # while True:
  #   for event in pygame.event.get():
  #     if event.type == pygame.QUIT:
  #       sys.exit()
  #   pygame.display.flip()

'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

# def get_nickname(screen, settings):
#   white = (255, 255, 255)
#   black = (0, 0, 0)
#   buttons_menu, buttons_pause, buttons_credits, buttons_lost = utils.list_buttons()
#   bg_y = 0
#   current_bg_index = 0
#   next_bg_index = random.randint(0, len(settings.background_images) - 1)
#   while True:
#     for event in pygame.event.get():
#       if event.type == pygame.QUIT:
#         sys.exit()
#       elif event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_RETURN:
#           print("Nickname: " + settings.nickname)
#           run_game()
#         elif event.key == pygame.K_BACKSPACE:
#           settings.nickname = settings.nickname[:-1]
#         else:
#           settings.nickname += event.unicode
  
#     screen.fill(white)
#     pygame.draw.rect(screen, black, (300, 300, 300, 50))
#     font = pygame.font.Font(None, 32)
#     bg_y, current_bg_index, next_bg_index = utils.update_background(settings, screen, bg_y, current_bg_index, next_bg_index)
#     text = font.render(settings.nickname, True, white)
#     screen.blit(text, (310, 310))
#     menu = utils.menu_load(screen, buttons_lost)
  
    # menu.run()
      
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

def pause_menu(screen, pause):
  
  # settings = Settings()
  buttons_menu, buttons_pause, buttons_credits, buttons_lost = utils.list_buttons()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
          # Cambiar la bandera de pausa
          return not pause
        if event.key == pygame.K_q:
          main_menu()
      elif event.type == pygame.MOUSEMOTION:
        for button in buttons_pause:
          button.check_hover(event.pos)
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          for button in buttons_pause:
            if button.is_hovered:
              button.perform_action()

    for button in buttons_pause:
      button.draw(screen)

    if not pygame.mixer.music.get_busy():
        play_music()

    pygame.display.flip()


'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
def lost_menu(screen):
  
  settings = Settings()
  pygame.mixer.Sound.play(settings.crash)
  buttons_menu, buttons_pause, buttons_credits, buttons_lost = utils.list_buttons()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          main_menu()
      elif event.type == pygame.MOUSEMOTION:
        for button in buttons_lost:
          button.check_hover(event.pos)
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          for button in buttons_lost:
            if button.is_hovered:
              button.perform_action()

    for button in buttons_lost:
      button.draw(screen)

    if not pygame.mixer.music.get_busy():
        play_music()

    pygame.display.flip()

    #Controla la velocidad de actualización de la pantalla
    

def play_music():
  pygame.mixer.music.set_volume(0.3)
  pygame.mixer.music.load(random.choice(songs))
  pygame.mixer.music.play()

def choose_car():
  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
  pygame.display.set_caption("TurboDash - ¡Choose your car!")
  cars = settings.cars
  select = 0

  fondo = pygame.image.load('./assets/img/backgrounds/background.png')

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          main_menu()
        elif event.key == pygame.K_LEFT:
          select = (select - 1) % len(cars)
        elif event.key == pygame.K_RIGHT:
          select = (select + 1) % len(cars)
        elif event.key == pygame.K_SPACE:
          run_game(car)

    option = cars[select]
    name = option["name"]
    car = option["car"]

    # Dibujar el fondo
    screen.blit(fondo, (0, 0))

    # Dibujar la imagen y el nombre del auto seleccionado
    screen.blit(name, (180, 200))  # Ajusta las coordenadas según tus necesidades
    screen.blit(car, (420, 400))   # Ajusta las coordenadas según tus necesidades

    if not pygame.mixer.music.get_busy():
        play_music()

    pygame.display.flip()



'''
If startup to call the main_menu() function.
'''
if __name__ == "__main__":
  main_menu()

