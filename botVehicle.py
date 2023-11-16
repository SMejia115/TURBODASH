import pygame
from pygame.sprite import Sprite

class BotVehicle(Sprite):

  def __init__(self, settings, screen, bot_image, pos_x, pos_y):
    super(BotVehicle, self).__init__()

    self.screen = screen
    self.settings = settings
    self.screen_rect = screen.get_rect()

    self.image = bot_image
    self.rect = self.image.get_rect()

    