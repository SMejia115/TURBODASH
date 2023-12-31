'''
TurboDash was created by Brayan Cataño Giraldo and Santiago Mejia Orejuela in 2023.
'''

'''
The pygame library is imported to load the car image.
'''
import pygame


'''
Car class with its respective attributes and methods. The input is sent settings and screen.
'''
class Car:
	def __init__(self, settings, screen, image):

		'''
		The screen, the settings, the image, the rectangle and the screen rectangle are initialized.
		'''
		self.screen = screen
		self.settings = settings
		self.image = image
		
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.center = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	'''
	The update(self, settings) method is used to update the position of the carriage depending 
	on the movement made.

	Function name: update
	Input: settings
	Output: None
	description: This function is used to update the position of the carriage depending
	'''
	def update(self, settings):
		if self.moving_right and self.rect.right < (self.screen_rect.right-settings.road_limit):
				self.center += self.settings.car_speed_factor

		if self.moving_left and self.rect.left > settings.road_limit:
				self.center -= self.settings.car_speed_factor

		self.rect.centerx = self.center

		if self.moving_up and self.rect.top > 0:
				self.bottom -= self.settings.car_speed_factor

		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
				self.bottom += self.settings.car_speed_factor

		self.rect.bottom = self.bottom

	'''
	The draw(self) method is used to draw the carriage.

	Function name: draw
	Input: None
	Output: None
	description: This function is used to draw the carriage.
	'''
	def draw(self):
		self.screen.blit(self.image, self.rect)