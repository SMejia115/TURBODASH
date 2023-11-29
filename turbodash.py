'''
TurboDash was created by Brayan Cataño Giraldo and Santiago Mejia Orejuela in 2023.
'''

'''
The pygame and sys library is imported to manage the TurboDash game and its system functions, 
as well as the files needed to run the game base.
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
The initial configuration parameters and statistics that will be used throughout the various screens 
of the game are initialized.
'''
settings = Settings()
stats = Stats(settings)
songs = settings.music

'''
The main_manu() function is the main function and is the one called when the game is started. 
It has no input or output parameters. It initializes pygame, the screen with its dimensions
and settings and the main menu of the game.
'''
def main_menu():
  # Pygame is initialized and the screen is set.
  pygame.init()
  pygame.mixer.init()
  settings = Settings()
  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
  pygame.display.set_caption("¡Welcome to Turbodash!")
  
  # The buttons for the main menu, pause, credits and lost are defined.
  buttons_menu, buttons_pause, buttons_credits, buttons_lost = utils.list_buttons()

  # The main menu is loaded.
  menu = utils.menu_load(screen, buttons_menu)

  # The main menu is executed. Here you will find event handling, background movement and drawing of buttons on the screen.
  menu.run()

'''
The run_game() function is the one that starts the game and is called after pressing the play button. 
It has no input or output parameters. It initializes the cart and calls the functions and classes in charge 
of the car and screen refresh functions.
'''
def run_game(image_car):
  # pygame.init()
  # Settings, screen, car and group bots are initialized.
  settings = Settings()
  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
  pygame.display.set_caption("TurboDash")
  car = Car(settings, screen, image_car)
  bots = Group()

# Initial configuration of the background.
  bg_y = 0
  current_bg_index = 0
  next_bg_index = random.randint(0, len(settings.background_images) - 1)

  # The game clock is initialized.
  clock = pygame.time.Clock()

  # The game time is initialized.
  pygame.time.set_timer(pygame.USEREVENT, settings.bot_generation_time)
  pygame.time.set_timer(pygame.USEREVENT+1, 10000)
  pygame.time.set_timer(pygame.USEREVENT+2, 200)

  # The bool pause is initialized.
  pause = False
	
  # Main game loop
  while True:
    # Checking keyboard events returning a Boolean value for pause
    pause = events.check_events(car, settings, screen, bots, pause, stats)
    utils.handle_power_up(settings, stats)
    # Verification of music playback
    if not pygame.mixer.music.get_busy():
        play_music()
    # Call to function pause_menu(screen, pause) in case pause equals True
    if pause:
      pause = pause_menu(screen, pause)
    # Calling the functions for updating motion and background drawing, carriage, bots, statistics and power.
    if not pause:
        car.update(settings)
        bg_y, current_bg_index, next_bg_index = events.refresh_screen(screen, car, settings, bg_y, current_bg_index, next_bg_index, bots, stats)


'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
The info_game() function is the function that presents the credits screen and additional game information 
and is called after pressing the info button. It has no input or output parameters. 
It initializes the menu class and calls the functions and classes in charge of the background 
and screen movement functions.
'''
def info_game():
  # pygame.init()
  # Settings and screen are initialized.
  settings = Settings()
  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
  pygame.display.set_caption("¡Credits TurboDash!")

  # The buttons for the main menu, pause, credits and lost are defined.
  buttons_menu, buttons_pause, buttons_credits, buttons_lost = utils.list_buttons()

  # The credits menu is loaded.
  menu = utils.menu_load(screen, buttons_credits)
  # The credits menu is executed. Here you will find event handling, background movement and drawing of buttons on the screen.
  menu.run()


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

'''
The pause_menu() function is the function that displays the pause screen and is called after pressing 
the p key on the keyboard in the middle of the game. It has the game screen and a boolean value pause. 
It returns the value of this changed boolean.
'''
def pause_menu(screen, pause):
  
  # The buttons for the main menu, pause, credits and lost are defined.
  buttons_menu, buttons_pause, buttons_credits, buttons_lost = utils.list_buttons()

  # Pause screen loop
  while True:
    # Verification of keyboard events for the output of this function to pause to the main menu or return to the game.
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
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

    # Drawing of buttons on the screen.
    for button in buttons_pause:
      button.draw(screen)

    # Verification of music playback
    if not pygame.mixer.music.get_busy():
        play_music()

    pygame.display.flip()


'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
The lost_menu() function is the function that displays the lost screen and is called after the car 
collides with another vehicle. It has the game screen. It calls the main_menu() function when pressing 
the q key on the keyboard.
'''
def lost_menu(screen):
  
  # Settings and screen and sound crash initialization.
  settings = Settings()
  pygame.mixer.Sound.play(settings.crash)

  # The buttons for the main menu, pause, credits and lost are defined.
  buttons_menu, buttons_pause, buttons_credits, buttons_lost = utils.list_buttons()

  # Lost screen loop
  while True:
    # Verification of keypad events for the output of this function to the main menu
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

    # Drawing of buttons on the screen.
    for button in buttons_lost:
      button.draw(screen)

    # Verification of music playback
    if not pygame.mixer.music.get_busy():
        play_music()

    pygame.display.flip()

'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
The play_music() function is the function that plays the game music and is called after pygame detects 
that the song it is playing is finished, playing a random song from the song list. 
It has no input or output parameters.
'''
def play_music():
  # The volume of music to be played is defined
  pygame.mixer.music.set_volume(0.3)
  # A random song is selected from the list of songs and played.
  pygame.mixer.music.load(random.choice(songs))
  # The song is played.
  pygame.mixer.music.play()

'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
The choose_car() function is the function that displays the car selection screen and is called 
after pressing the play button. It has no input or output parameters. From there, it calls main_menu() 
again by pressing the q key on the keyboard and selects one of the cars by pressing the space key on 
the keyboard, calling the function run_game(car) sending it the selected car.
'''
def choose_car():
  # Screen and dictionary of car names and images initialization.
  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
  pygame.display.set_caption("TurboDash - ¡Choose your car!")
  cars = settings.cars
  select = 0

  # Background image loading.
  background = pygame.image.load('./assets/img/backgrounds/background.png')

  # loop for the selection of cars
  while True:
    # Keyboard event verification for the output of this function to the game.
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

    # The selected car is loaded.
    option = cars[select]
    name = option["name"]
    car = option["car"]

    # The background is drawn on the screen.
    screen.blit(background, (0, 0))

    # The car and its name are drawn on the screen.
    screen.blit(name, (180, 200))  
    screen.blit(car, (420, 400))   

    # Verification of music playback
    if not pygame.mixer.music.get_busy():
        play_music()

    pygame.display.flip()

'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
If startup to call the main_menu() function.
'''
if __name__ == "__main__":
  main_menu()

