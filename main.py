import sys
import pygame

from window import window
from player import player

def main():
	pygame.init()
	window.open()

	game_runned = True

	while game_runned:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		player.draw(window.get_window)
		window.update()

if __name__ == "__main__":
	main()