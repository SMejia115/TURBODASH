'''
TurboDash was created by Brayan Cataño Giraldo and Santiago Mejia Orejuela in 2023.
'''

'''
The pygame and sys library is imported to manage TurboDash utilities such as image loading, 
button creation and others, also its system functions, as well as the files needed to execute these tasks.
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
import math

'''
The settings class is initialized.
'''
settings = Settings()

'''
The pygame.mixer library is imported to play the background music of the game.
'''
pygame.mixer.init()

'''
The list_buttons() function is the function in charge of creating the buttons and 
adding them to a list of buttons. It has no input parameters and as output parameters 
it has the list of buttons.

Function name: list_buttons
Input: None
Output: None
description: This function is used to create the buttons and add them to a list of buttons.

'''
def list_buttons():
  settings = Settings()
  #Bottons menu start
  tittle_start_button = Button(250, 100, 500, 100, pygame.image.load("./assets/img/logo/Td.png"), pygame.image.load("./assets/img/logo/Td.png"), None)
  play_start_button = Button(380, 300, 150, 50, pygame.image.load("./assets/img/buttons/play1.png"), pygame.image.load("./assets/img/buttons/play2.png"), td.choose_car)
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
The function menu_load(screen, buttons) is the function in charge of creating the menu. 
It has screen and buttons as input parameters and as output parameters it has the created menu.

Function name: menu_load
Input: screen, buttons
Output: None
description: This function is used to create the menu.

'''
def menu_load(screen, buttons):
  menu = Menu(screen, buttons, pygame.image.load("./assets/img/roads/forestRoad1.png"))
  return menu

'''
The function pause_load(screen, buttons) is the function in charge of creating the pause menu.
It has screen and buttons as input parameters and as output parameters it has the created pause menu.

Function name: pause_load
Input: screen, buttons
Output: None
description: This function is used to create the pause menu.

'''
def pause_load(screen, buttons):
  pause = Menu(screen, buttons, pygame.image.load("./assets/img/backgrounds/1.jpg"))
  return pause

'''
The road_image(screen) function is the function responsible for displaying the road. 
It has no input or output parameters.

Function name: road_image
Input: screen
Output: None
description: This function is used to display the road.

'''
def road_image(screen, settings):
  bg_y = 0
  current_bg_index = 0
  next_bg_index = random.randint(0, len(settings.background_images) - 1)

  bg_y, current_bg_index, next_bg_index = update_background(settings, screen, bg_y, current_bg_index, next_bg_index)

  # background_image = pygame.image.load('./assets/img/roads/forestRoad1.png')
  # screen.blit(background_image, (0, 0))

'''
The car_image() function is the function responsible for loading the image of the car and 
giving it transparency

Function name: car_image
Input: None
Output: None
description: This function is used to load the image of the car and give it transparency

'''
def car_image():
  car = pygame.image.load("./assets/img/cars/car2.png")
  # .convert()
  # car.set_colorkey(settings.car_colorkey)
  return car

'''
Function update_background(settings, screen) is the function in charge of updating the 
background image. It has screen and settings as input parameters and as output parameters it 
has the updated background image.

Function name: update_background
Input: settings, screen
Output: None
description: This function is used to update the background image.

'''
def update_background(settings, screen, bg_y, current_bg_index, next_bg_index):
  bg_y += settings.bg_speed
  # If the background moves off the screen, restart it
  if bg_y >= settings.screen_height:
    # Change the current image to the next one
    current_bg_index = next_bg_index
    # Select a new image for next
    next_bg_index = random.randint(0, len(settings.background_images) - 1)
    # Reset background position
    bg_y = 0

  # Draw the background on the screen
  screen.blit(settings.background_images[current_bg_index], (0, bg_y))
  screen.blit(settings.background_images[next_bg_index], (0, bg_y - settings.screen_height))
  return bg_y, current_bg_index, next_bg_index


'''
Function generate_bot(settings, screen, bots) is the function in charge of generating the bots. 
It has screen, settings and bots as input parameters and as output parameters 
it has the generated bots.

Function name: generate_bot
Input: settings, screen, bots
Output: None
description: This function is used to generate the bots.

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

'''
Function update_bots(bots, settings, car, screen, stats) is the function in charge of updating the bots.
It has bots, settings, car, screen and stats as input parameters and as output parameters
it has the updated bots.

Function name: update_bots
Input: bots, settings, car, screen, stats
Output: None
description: This function is used to update the bots.

'''
def update_bots(bots, settings, car, screen, stats):
  activated_bots=[]
  for bot in bots.copy():
    bot.update(settings)
    if bot.rect.top >= settings.screen_height:
      bots.remove(bot)
      #print("Bot deleted")
  check_distance(car, bots, stats)
  colision = check_collisions(car, bots)
  if colision:
    bots.empty()
    settings.bg_speed = 5
    settings.bot_generation_time = 10000
    # print("Bots deleted")
    stats.reset_score()
    td.lost_menu(screen)
    return True

'''
Function draw_bots(bots) is the function in charge of drawing the bots.
It has bots as input parameters and as output parameters
it has the drawn bots.

Function name: draw_bots
Input: bots
Output: None
description: This function is used to draw the bots.
'''
def draw_bots(bots):
  for bot in bots.sprites():
    bot.draw()

'''
Function check_collisions(car, bots) is the function in charge of checking the collisions.
It has car and bots as input parameters and as output parameters
it has the collisions checked.

Function name: check_collisions
Input: car, bots
Output: None
description: This function is used to check the collisions.

'''
def check_collisions(car, bots):
  if pygame.sprite.spritecollideany(car, bots):
    # print("Car crashed")
    return True
  return False

'''
Function check_distance(car, bots, stats) is the function in charge of checking the distance.
It has car, bots and stats as input parameters and as output parameters
it has the distance checked.

Function name: check_distance
Input: car, bots, stats
Output: None
description: This function is used to check the distance.


'''
def check_distance(car, bots, stats):

    for bot in bots.sprites():
        distance_x = abs(bot.rect.centerx - car.rect.centerx)
        distance_y = abs(bot.rect.centery - car.rect.centery)

        # Distancia euclidiana
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if distance < 100 and bot not in stats.activated_bots and stats.power_quantity <= 5:
        # if abs(bot.rect.centerx - car.rect.centerx) < 70 and abs(bot.rect.bottom - car.rect.bottom) and bot not in stats.activated_bots:
            pygame.mixer.Sound.play(settings.power_up)
            stats.update_power_quantity()
            stats.activated_bots.add(bot)
            

'''
Handle Power Up

Function name: handle_power_up
Input: settings, stats
Output: None
description: This function is used to handle the power up.

'''

def handle_power_up(settings, stats):
        stats.decrease_power_quantity()
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - stats.power_up_time
        stats.power_quantity = 0

        if elapsed_time < stats.power_duration:
            # Si el poder está activo, disminuye la velocidad del fondo
            settings.bg_speed = 2  # Ajusta esto según tus 
            settings.bot_generation_time = 10000
        else:
            # Si el poder ha terminado, restablece la velocidad del fondo
            settings.bg_speed = 5
            stats.power_up = False
            settings.bot_generation_time = 1000
