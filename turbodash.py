import pygame 
import sys
from button import Button
from menu import Menu

def main_menu():
  pygame.init()
  screen = pygame.display.set_mode((800, 600))
  pygame.display.set_caption("TurboDash")
  
  play_button = Button(300, 200, 200, 50, pygame.image.load("./assets/img/playButton1.png"), pygame.image.load("./assets/img/playButton2.png"), None)
  quit_button = Button(300, 300, 200, 50, pygame.image.load("./assets/img/exitButton1.png"), pygame.image.load("./assets/img/exitButton2.png"), sys.exit)
  buttons = [play_button, quit_button]

  menu = Menu(screen, buttons, pygame.image.load("./assets/img/background.png"))
  menu.run()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.flip()





if __name__ == "__main__":
    main_menu()