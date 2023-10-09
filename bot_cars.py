import pygame
from pygame.sprite import Sprite

class bot(Sprite):
    def __init__(self, screen, image):
        super(bot, self).__init__()

        self.screen = screen

        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def draw(self):
        self.screen.blit(self.image, self.rect)