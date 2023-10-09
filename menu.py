'''
The pygame and sys library is imported for the correct functioning of the game menu.
'''
import pygame
import sys

'''
Menu class with its respective attributes and methods. In input, the screen, the buttons and the background image are sent to it.
'''
class Menu:
  def __init__(self, screen, buttons, background_img):
    self.screen = screen
    self.buttons = buttons
    self.background_img = background_img

  '''
  Method check_events(self) is used to check what is being done with the buttons shown in the menu and what to do with that event.
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
              button.perform_action()

  '''
  Method draw(self) is used to draw the menu with its respective image and buttons.
  '''
  def draw(self):
    self.screen.blit(self.background_img, (0, 0))
    for button in self.buttons:
      button.draw(self.screen)
    pygame.display.flip()

  '''
  Method run(self) is used to call the other methods.
  '''
  def run(self):
    while True:
      self.check_events()
      self.draw()