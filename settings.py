'''
TurboDash was created by Brayan Cataño Giraldo and Santiago Mejia Orejuela in 2023.
'''

'''
Pygame initialization.
'''
import pygame

'''
Pygame mixer initialization.
'''
pygame.mixer.init()

'''
Settings class with its respective setting attributes.
'''
class Settings:
  def __init__(self):
    '''
    The screen width and height, the car speed factor, the car colorkey, the road limit, 
    the background images, the bot images, the cars, the crash, the car, the horn, 
    the power up, the music, the background speed, the bot generation time, the nickname,
    the score and the high score are initialized.
    '''
    self.screen_width = 910
    self.screen_height = 700

    
    self.car_speed_factor = 7
    self.car_colorkey = (255, 255, 255)
    self.road_limit = 245

    self.background_images = [pygame.image.load('./assets/img/roads/snowRoad1.png'),
                  pygame.image.load('./assets/img/roads/snowRoad2.png'),
                  pygame.image.load('./assets/img/roads/forestRoad2.png'),
                  pygame.image.load('./assets/img/roads/forestRoad1.png')]
    
    self.bot_images = [pygame.image.load('./assets/img/cars/car1.png'),
                pygame.image.load('./assets/img/cars/car2.png'),
                pygame.image.load('./assets/img/cars/car3.png'),
                pygame.image.load('./assets/img/cars/car4.png'),
                pygame.image.load('./assets/img/cars/car5.png'),
                pygame.image.load('./assets/img/cars/car6.png')]
    
    self.cars = [{"name": pygame.image.load('./assets/img/cars/nameCar1.png'), "car": pygame.image.load('./assets/img/cars/car1.png')},
                {"name": pygame.image.load('./assets/img/cars/nameCar2.png'), "car": pygame.image.load('./assets/img/cars/car2.png')},
                {"name": pygame.image.load('./assets/img/cars/nameCar3.png'), "car": pygame.image.load('./assets/img/cars/car3.png')},
                {"name": pygame.image.load('./assets/img/cars/nameCar4.png'), "car": pygame.image.load('./assets/img/cars/car4.png')},
                {"name": pygame.image.load('./assets/img/cars/nameCar5.png'), "car": pygame.image.load('./assets/img/cars/car5.png')},
                {"name": pygame.image.load('./assets/img/cars/nameCar6.png'), "car": pygame.image.load('./assets/img/cars/car6.png')}]

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

    


    