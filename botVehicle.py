import pygame
from pygame.sprite import Sprite

class BotVehicle(Sprite):

  def __init__(self, settings, screen, bot_image, pos_x, pos_y, direction):
    super(BotVehicle, self).__init__()

    self.screen = screen
    self.settings = settings
    self.screen_rect = screen.get_rect()

    self.image = bot_image
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

    self.center = float(self.rect.centerx)
    self.bottom = float(self.rect.bottom)

  def update(self, settings):
    if self.direction == 1:
      self.center += settings.bot_speed_factor
    else:
      self.center -= settings.bot_speed_factor

    self.rect.centerx = self.center

  def draw(self):
    self.screen.blit(self.image, self.rect)


  