from pygame import display

class Window:
	def __init__(self, caption, size: tuple):
		self.__caption = caption
		self.__size = size

	def open(self):
		global screen
		screen = display.set_mode(self.__size)
		display.set_caption(self.__caption)

	def update(self):
		display.update()

	@property
	def get_window(self):
		return screen


window = Window("Game by RusIvanDen & KadenCode", (500, 500))