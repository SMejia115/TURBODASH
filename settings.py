'''
Settings class with its respective setting attributes.
'''
import pygame

pygame.mixer.init()

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
        
        self.cars = [{"name": pygame.image.load('./assets/img/bots/nameBot1.png'), "car": pygame.image.load('./assets/img/bots/bot1.png')},
                    {"name": pygame.image.load('./assets/img/bots/nameBot2.png'), "car": pygame.image.load('./assets/img/bots/bot2.png')},
                    {"name": pygame.image.load('./assets/img/bots/nameBot3.png'), "car": pygame.image.load('./assets/img/bots/bot3.png')},
                    {"name": pygame.image.load('./assets/img/bots/nameBot4.png'), "car": pygame.image.load('./assets/img/bots/bot4.png')},
                    {"name": pygame.image.load('./assets/img/bots/nameBot5.png'), "car": pygame.image.load('./assets/img/bots/bot5.png')},
                    {"name": pygame.image.load('./assets/img/bots/nameBot6.png'), "car": pygame.image.load('./assets/img/bots/bot6.png')}]
    
        self.crash = pygame.mixer.Sound("./assets/sounds/car-explosion.mp3")
        self.car = pygame.mixer.Sound("./assets/sounds/car_engine.mp3")
        self.horn = pygame.mixer.Sound("./assets/sounds/car-horn.mp3")
        self.power_up = pygame.mixer.Sound("./assets/sounds/power_up.mp3")
        
        self.music = ['./assets/sounds/music/FeelTheRushJunkieXLRemixElectroVersion.mp3',
                    './assets/sounds/music/MyFriendDarioElectro.mp3',
                    './assets/sounds/music/RideAWhiteHorse.mp3',
                    './assets/sounds/music/Steamworks.mp3',
                    './assets/sounds/music/WashingUpTiga.mp3']
        
        self.bg_speed = 5

        self.bot_generation_time = 1000

        # Scoreboard settings

        self.nickname = ''
        self.score = 0
        self.high_score = 0

        self.call_power = False

        


        