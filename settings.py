'''
Settings class with its respective setting attributes.
'''
import pygame

class Settings:

    def __init__(self):
        self.screen_width = 910
        self.screen_height = 700

        self.car_speed_factor = 7
        self.car_colorkey = (255, 255, 255)
        self.road_limit = 245

        self.background_images = [pygame.image.load('./assets/img/roads/snowRoad1.png'),
                     pygame.image.load('./assets/img/roads/snowRoad2.png'),
                     pygame.image.load('./assets/img/roads/forestRoad2.png'),
                     pygame.image.load('./assets/img/roads/forestRoad1.png')]
        
        self.bot_images = [pygame.image.load('./assets/img/bots/bot1.png'),
                    pygame.image.load('./assets/img/bots/bot2.png'),
                    pygame.image.load('./assets/img/bots/bot3.png'),
                    pygame.image.load('./assets/img/bots/bot4.png'),
                    pygame.image.load('./assets/img/bots/bot5.png'),
                    pygame.image.load('./assets/img/bots/bot6.png')]
        
        
        
        self.bg_speed = 5

        self.bot_generation_time = 1000

        