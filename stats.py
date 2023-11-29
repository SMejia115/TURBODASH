'''
TurboDash was created by Brayan Cataño Giraldo and Santiago Mejia Orejuela in 2023.
'''

'''
The pygame and os library imported for the correct functioning of the game.
'''
import os
import pygame

class Stats:
  '''
  Statistics class with its respective attributes and methods. The input is sent settings.
  '''
  '''
  The settings, the game active, the high score, the score, the nickname, the font1, the font2,
  the power quantity, the power duration and the activated bots are initialized.

  Function name: __init__
  Input: settings
  Output: None
  description: The settings, the game active, the high score, the score, the nickname, the font1, the font2,
  the power quantity, the power duration and the activated bots are initialized.

  '''
  def __init__(self, settings):
    self.settings = settings
    self.reset_score()
    self.game_active = False
    self.high_score = 0
    self.score = 0
    self.nickname = ''
    self.font1 = os.path.join('./assets/fonts/8_bit_arcade', '8-bit Arcade in.ttf')
    self.font2 = os.path.join('./assets/fonts/8_bit_arcade', '8-bit Arcade Out.ttf')
    self.power_quantity = 0
    self.power_duration = 100
    self.activated_bots = set()

    self.power_images = [pygame.image.load('./assets/img/power/1.png'),
                        pygame.image.load('./assets/img/power/2.png'),
                            pygame.image.load('./assets/img/power/3.png'),
                            pygame.image.load('./assets/img/power/4.png'),
                            pygame.image.load('./assets/img/power/5.png'),
                            pygame.image.load('./assets/img/power/6.png')
    ]
    
    self.power_up = False

    self.power_up_time = 0

  '''
  The update_nickname(self, nickname) method is used to update the nickname.

  Function name: update_nickname
  Input: nickname
  Output: None
  description: This function is used to update the nickname.

  '''
  def update_nickname(self, nickname):
    self.nickname = nickname

  '''
  The update_high_score(self, score) method is used to update the high score.

  Function name: update_high_score
  Input: score
  Output: None
  description: This function is used to update the high score.

  '''
  def update_high_score(self, score):
    if score > self.high_score:
      self.high_score = score
  
  '''
  The update_stats(self, score) method is used to update the statistics.

  Function name: update_stats
  Input: score
  Output: None
  description: This function is used to update the statistics.

  '''
  def update_stats(self, score):
    self.update_high_score(self.score)
    self.score += score

  '''
  The update_power_quantity(self) method is used to update the power quantity.

  Function name: update_power_quantity
  Input: None
  Output: None
  description: This function is used to update the power quantity.

  '''
  def update_power_quantity(self):
    if self.power_quantity < 5:
      self.power_quantity += 1

  '''
  The draw_power_quantity(self) method is used to draw the power quantity.

  Function name: draw_power_quantity
  Input: None
  Output: None
  description: This function is used to draw the power quantity.
  '''
  def draw_power_quantity(self, screen):
    screen.blit(self.power_images[self.power_quantity], (self.settings.screen_width - 200, 150))    

  '''
  The draw_score(self) method is used to draw the score.

  Function name: draw_score
  Input: None
  Output: None
  description: This function is used to draw the score.

  '''
  def draw_score(self, screen):
    '''
    The font1, font2 and scores are initialized.
    '''
    font1 = pygame.font.Font(self.font1, 35)
    font2 = pygame.font.Font(self.font2, 35)
    score1 = font1.render(f'SCORE {self.score}', True, (255, 255, 255))
    score2 = font2.render(f'SCORE {self.score}', True, (237,185,2))
    score1_rect = score1.get_rect()
    score2_rect = score2.get_rect()
    score1_rect.center = (self.settings.screen_width - 100, 50)
    score2_rect.center = (self.settings.screen_width - 100, 52)

    max_score = self.high_score
    high_score1 = font1.render(f'HIGH SCORE {max_score}', True, (255, 255, 255))
    high_score2 = font2.render(f'HIGH SCORE {max_score}', True, (237,185,2))
    max_score1_rect = high_score1.get_rect()
    max_score2_rect = high_score2.get_rect()

    max_score1_rect.center = (115, 50)
    max_score2_rect.center = (115, 52)

  '''
  Function name: update_stats
  Input: score
  Output: None
  description: This function is used to update the statistics.
  '''
  def update_stats(self, score): 
    self.update_high_score(self.score)
    self.score += score

  '''
  Function name: update_power_quantity
  Input: None
  Output: None
  description: This function is used to update the power quantity.

  '''
    
  def update_power_quantity(self):
    if self.power_quantity < 5:
        self.power_quantity += 1


  '''
  Function name: decrease_power_quantity
  Input: None
  Output: None
  description: This function is used to decrease the power quantity.
  '''
  def decrease_power_quantity(self): 
    if self.power_quantity > 0:
        print(self.power_quantity)
        self.power_quantity -= 5
        print("Se disminuyó: ", self.power_quantity)
    
  '''
  Function name: draw_power_quantity
  Input: None
  Output: None
  description: This function is used to draw the power quantity.
  '''
  def draw_power_quantity(self, screen):
      screen.blit(self.power_images[self.power_quantity], (self.settings.screen_width - 200, 150))    


  '''
  Function name: draw_score
  Input: None
  Output: None
  description: This function is used to draw the score.
  
  '''
  def draw_score(self, screen):
    font1 = pygame.font.Font(self.font1, 35)
    font2 = pygame.font.Font(self.font2, 35)
    score1 = font1.render(f'SCORE {self.score}', True, (255, 255, 255))
    score2 = font2.render(f'SCORE {self.score}', True, (237,185,2))
    score1_rect = score1.get_rect()
    score2_rect = score2.get_rect()
    score1_rect.center = (self.settings.screen_width - 100, 50)
    score2_rect.center = (self.settings.screen_width - 100, 52)

    max_score = self.high_score
    high_score1 = font1.render(f'HIGH SCORE {max_score}', True, (255, 255, 255))
    high_score2 = font2.render(f'HIGH SCORE {max_score}', True, (237,185,2))
    max_score1_rect = high_score1.get_rect()
    max_score2_rect = high_score2.get_rect()

    max_score1_rect.center = (115, 50)
    max_score2_rect.center = (115, 52)
    
    '''
    The scores are drawn on the screen.
    '''
    screen.blit(score2, score2_rect)
    screen.blit(score1, score1_rect)
    screen.blit(high_score2, max_score2_rect)
    screen.blit(high_score1, max_score1_rect)



  '''
  The reset_stats(self) method is used to reset the statistics.
  '''
  def reset_score(self):
    self.power_quantity = 0
    self.score = 0

  '''
  The save_score(self) method is used to save the score.
  '''
  def save_score(self):
    with open('./assets/high_scores.txt', 'a') as file:
      file.write(f'{self.nickname} {self.score}\n')

  '''
  The get_high_score(self) method is used to get the high score.
  '''
    # def get_high_score(self):
    #     with open('./assets/high_scores.txt', 'r') as file:
    #         for line in file:
    #             if line != '':
    #                 score = line.split(' ')[1]
    #                 if int(score) > self.high_score:
    #                     self.high_score = int(score)
    #     return self.high_score

  def get_high_score(self):
    if self.score >= self.high_score:
      self.high_score = self.score

  def activate_power(self):
    if self.power_quantity == 5:
      self.power_up = True
      self.power_up_time = pygame.time.get_ticks()
      self.power_quantity = 0  # Gasta todo el acumulado

  def handle_power(self, settings):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.power_up_time

        if elapsed_time < 5000:  # 5000 milisegundos = 5 segundos
            # Si el poder está activo, disminuye la velocidad del fondo
            settings.bg_speed = 1.5
        else:
            # Si el poder ha terminado, restablece la velocidad del fondo
            settings.bg_speed = 5
            self.power_up = False