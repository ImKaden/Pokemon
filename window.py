import pygame

class Window:
	def __init__(self, bg: tuple, size: tuple, mode=pygame.RESIZABLE):
		self.mode = mode
		self.size = size
		self.background = bg
		self.window = pygame.display.set_mode(self.size, self.mode)

	def set_caption(self, caption):
		pygame.display.set_caption(caption)

	def update(self):
		pygame.display.update()

	def fill(self):
		self.window.fill(self.background)

window = Window((42, 0, 0), (0, 0), pygame.FULLSCREEN)