'''
TurboDash was created by Brayan Cataño Giraldo and Santiago Mejia Orejuela in 2023.
'''

'''
The pygame and sys library is imported for the correct functioning of the game menu.
'''
import pygame
import sys
import utils 
from settings import Settings
import random 
import turbodash as td

'''
Menu class with its respective attributes and methods. In input, the screen, the buttons 
and the background image are sent to it.
'''
class Menu:
  def __init__(self, screen, buttons, background_img):
    self.screen = screen
    self.buttons = buttons
    self.background_img = background_img
    self.settings = Settings()
  
  '''
  Method check_events(self) is used to check what is being done with the buttons shown in 
  the menu and what to do with that event.

  Function name: check_events
  Input: None
  Output: None
  description: This function is used to check what is being done with the buttons shown in
  the menu and what to do with that event.

  '''
  def check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEMOTION:
        for button in self.buttons:
          button.check_hover(event.pos)
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          for button in self.buttons:
            if button.is_hovered:
              pygame.mixer.music.pause()
              button.perform_action()

  '''
  Method draw(self) is used to draw the menu with its respective image and buttons.

  Function name: draw
  Input: None
  Output: None
  description: This function is used to draw the menu with its respective image and buttons.

  '''
  def draw(self):
    utils.update_background(self.screen, self.settings)
    # self.screen.blit(self.background_img, (0, 0))
    for button in self.buttons:
      button.draw(self.screen)
    pygame.display.flip()

  '''
  Method run(self) is used to call the other methods.

  Function name: run
  Input: None
  Output: None
  description: This function is used to call the other methods.

  '''
  def run(self):
    bg_y = 0
    current_bg_index = 0
    next_bg_index = random.randint(0, len(self.settings.background_images) - 1)
    while True:
      # Move the background
      bg_y, current_bg_index, next_bg_index = utils.update_background( self.settings, self.screen, bg_y, current_bg_index, next_bg_index)

      # Verify events
      self.check_events() 

      # Draw the buttons
      for button in self.buttons:
        button.draw(self.screen)
      
      # Verification of music playback
      if not pygame.mixer.music.get_busy():
        td.play_music()

      pygame.display.flip()