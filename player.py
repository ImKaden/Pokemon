import pygame

from window import window

class Player:
	def __init__(self, speed, health):
		self.window = window.window

		self.speed = speed
		self.health = health
		self.sprite = pygame.image.load("images/player.png")
		
		self.rect = self.sprite.get_rect()
		self.window_rect = self.window.get_rect()
		self.rect.centerx = self.window_rect.centerx
		self.rect.bottom = self.window_rect.bottom

	def draw(self):
		self.window.blit(self.sprite, self.rect)

	def move(self, side):
		if side == "UP":
			self.rect.bottom -= self.speed
		if side == "DOWN":
			self.rect.bottom += self.speed
		if side == "RIGHT":
			self.rect.centerx += self.speed
		if side == "LEFT":
			self.rect.centerx -= self.speed

player = Player(5, 1)