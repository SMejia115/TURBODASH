import pygame 
import sys
from settings import Settings
import utils

def main_menu():
  pygame.init()
  settings = Settings()
  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
  pygame.display.set_caption("TurboDash")
  
  buttons = utils.list_buttons()

  menu = utils.menu_load(screen, buttons)
  menu.run()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.flip()





if __name__ == "__main__":
    main_menu()