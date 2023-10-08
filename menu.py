import pygame
import sys

class Menu():
  def __init__(self, screen, buttons, background_img):
    self.screen = screen
    self.buttons = buttons
    self.background_img = background_img

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

  def draw(self):
    self.screen.blit(self.background_img, (0, 0))
    for button in self.buttons:
      button.draw(self.screen)
    pygame.display.flip()

  def run(self):
    while True:
      self.check_events()
      self.draw()
  