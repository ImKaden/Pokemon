import sys
import pygame

from window import window
from player import player
from controls import controls

class Game():
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		self.clock = pygame.time.Clock()

	def main(self):
		window.set_caption("Game by DeathGodMash & KadenCode")

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			
			controls.movement_events()

			self.clock.tick(60)

			window.fill()
			
			player.draw()
			
			window.update()


game = Game()

if __name__ == "__main__":
	game.main()