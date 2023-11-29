'''
TurboDash was created by Brayan Cataño Giraldo and Santiago Mejia Orejuela in 2023.
'''

'''
The pygame library is imported to adapt the rectangle of the buttons.
'''
import pygame

'''
Button class with its respective attributes and methods. On input, it is sent the x-position, 
y-position, width, height, image, hover image and the action to be performed by the button.
'''
class Button:
	def __init__(self, x, y, width, height, image, hover_image, action):
		self.rect = pygame.Rect(x, y, width, height)
		self.image = image
		self.hover_image = hover_image
		self.action = action
		self.is_hovered = False

	'''
  The draw(self, screen) method is used to draw the button depending on the screen dimensions to be used.
  '''	
	def draw(self, screen):
		if self.is_hovered:
			screen.blit(self.hover_image, self.rect.topleft)
		else:
			screen.blit(self.image, self.rect.topleft)

	'''
  The check_hover(self, screen) method is used to check whether to display the hover image.
  '''
	def check_hover(self, pos):
		self.is_hovered = self.rect.collidepoint(pos)

	'''
  The perform_action(self, screen) method is used to call the action to be performed.
  '''
	def perform_action(self):
		if self.action is not None:
				self.action()
		else:
				print("No action assigned to button")