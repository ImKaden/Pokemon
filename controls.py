import sys
import pygame

from player import player

class Controls:
	def movement_events(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			player.move("UP")
		if keys[pygame.K_DOWN]:
			player.move("DOWN")
		if keys[pygame.K_RIGHT]:
			player.move("RIGHT")
		if keys[pygame.K_LEFT]:
			player.move("LEFT")

controls = Controls()