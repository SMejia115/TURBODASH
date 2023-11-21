import pygame
from pygame.sprite import Sprite

class BotVehicle(Sprite):

  def __init__(self, settings, screen, bot_image, direction, rail):
    super(BotVehicle, self).__init__()

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

    if self.direction == 1:
      self.rect.bottom = 0
      self.image = pygame.transform.flip(self.image, False, True)
    else:
      self.rect.bottom = self.screen_rect.bottom + self.rect.height

    self.center = float(self.rect.centerx)
    self.bottom = float(self.rect.bottom)

  def update(self, settings):
    if self.direction == 1:
      self.bottom += (settings.bg_speed-1)
    else:
      self.bottom -= (settings.bg_speed-1)

    self.rect.bottom = self.bottom

  def draw(self):
    self.screen.blit(self.image, self.rect)


  