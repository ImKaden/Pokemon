import pygame
from window import window

class Player:
	def __init__(self, color: tuple, properties: tuple):
		self.__color = color
		self.__properties = properties

	def draw(self, window):
		pygame.draw.rect(window, self.__color, self.__properties)


player = Player((247, 240, 22), (150, 150, 150, 150))