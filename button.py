import pygame

class Button:
	def __init__(self, x, y, width, height, image, hover_image, action):
		self.rect = pygame.Rect(x, y, width, height)
		self.image = image
		self.hover_image = hover_image
		self.action = action
		self.is_hovered = False

	def draw(self, screen):
		if self.is_hovered:
			screen.blit(self.hover_image, self.rect.topleft)
		else:
			screen.blit(self.image, self.rect.topleft)

	def check_hover(self, pos):
		self.is_hovered = self.rect.collidepoint(pos)

	def perform_action(self):
		if self.action is not None:
				self.action()
		else:
				print("No action assigned to button")