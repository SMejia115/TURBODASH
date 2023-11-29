'''
TurboDash was created by Brayan Cataño Giraldo and Santiago Mejia Orejuela in 2023.
'''

'''
Pygame and sprite are imported for the operation of the bots and groups of bots.
'''
import pygame
from pygame.sprite import Sprite

'''
The BotVehicle class is created, which inherits from the Sprite class.
'''
class BotVehicle(Sprite):

  '''
  The constructor is defined, which receives the settings, the screen, the bot image, 
  the direction and the rail.
  '''
  def __init__(self, settings, screen, bot_image, direction, rail):
    super(BotVehicle, self).__init__()

    '''
    The screen, the settings, the screen rectangle, the direction, the image, the rectangle,
    the screen rectangle, the rail and the rails are initialized.
    '''
    self.screen = screen
    self.settings = settings
    self.screen_rect = screen.get_rect()
    self.direction = direction
    self.image = bot_image
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    self.rail = rail
    self.rails = [265, 370, 480, 580]
    self.rect.centerx= self.rails[self.rail] + self.rect.width/2

    '''
    The position of the bot is defined according to the direction.
    '''
    if self.direction == 1:
      self.rect.bottom = 0
      self.image = pygame.transform.flip(self.image, False, True)
    else:
      self.rect.bottom = self.screen_rect.bottom + self.rect.height

    self.center = float(self.rect.centerx)
    self.bottom = float(self.rect.bottom)

  '''
  The update method is defined, which receives the settings.

  Function name: update
  Input: settings
  Output: None
  description: This function is used to update the bot.
  '''
  def update(self, settings):
    if self.direction == 1:
      self.bottom += (settings.bg_speed+2)
    else:
      self.bottom -= (settings.bg_speed-1)

    self.rect.bottom = self.bottom

  '''
  The draw method is defined, which draws the bot on the screen.

  Function name: draw
  Input: None
  Output: None
  description: This function is used to draw the bot on the screen.
  
  '''
  def draw(self):
    self.screen.blit(self.image, self.rect)