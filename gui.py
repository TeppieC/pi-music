import sys, pygame, random
import asset
from pygame import Surface
from pygame import time

pygame.init()
pygame.font.init()
FONT_SIZE = 30
FONT = pygame.font.SysFont("Mono", FONT_SIZE, True)
PUP_FONT_SIZE = 20
PUP_FONT = pygame.font.SysFont("Arial", PUP_FONT_SIZE, True)

pygame.mixer.init()

class GUI(pygame.Surface):

	def __init__(self, screen_size_tuple, path):

		pygame.Surface.__init__(self, size = screen_size_tuple)
		self.screen = pygame.display.set_mode(screen_size_tuple, 0, 0)
		pygame.display.set_caption("Music")

		self._width = screen_size_tuple[0] #480
		self._height = screen_size_tuple[1] #320
		print(self._height, self._width)
		
		self._rect_screen = screen_size_tuple # size of the window
		self._rect_caption = pygame.Rect(0, 0, self._width, self._height/4)
		self._rect_controls = pygame.Rect(0, self._height/4, self._width, (self._height*3)/4)

		self._rect_rollback = pygame.Rect(0, self._height/4, self._width/4, (self._height*3)/4)

		self._rect_center = pygame.Rect(self._width/4, self._height/4, self._width/2, (self._height*3)/4)
		self._rect_vol_up = pygame.Rect(self._width/4, self._height/4, self._width/2, self._height/4)
		self._rect_pause = pygame.Rect(self._width/4, self._height/2, self._width/2, self._height/4)
		self._rect_vol_down = pygame.Rect(self._width/4, (self._height*3)/4, self._width/2, self._height/4)
		
		self._rect_forward = pygame.Rect((self._width*3)/4, self._height/4, self._width/4, (self._height*3)/4)
		self.music_list = self.music_setup(path)
		self.current_song_index = 0
		
		self.screen.fill((122,122,122), self._rect_rollback)

		print("songs/%s"%self.music_list[self.current_song_index])
		#pygame.mixer.music.load("songs/%s"%self.music_list[self.current_song_index])

		#pygame.mixer.music.play(-1, 0.0)
		#while pygame.mixer.music.get_busy(): 
		#	pygame.time.Clock().tick(10)

		print(self._rect_rollback)
		print(self._rect_center)
		print(self._rect_forward)
		self.load_image(self._rect_rollback, "rollback1.png")
		self.load_image(self._rect_center, "start1.png")
		self.load_image(self._rect_forward, "forward1.png")


	def music_setup(self, path):
		songs = []
		with open(path, 'r') as f:
			songs = f.readlines()
		return songs

	
	def is_in_rect(self, x, y, rect):
		'''
		Check and return whether given position(x, y)
		is located inside of the specified rect

		Args:
		x, y(int): the postion to be checked if located in rect
		
		rect(pygame.Rect): the rectangle to be checked if 
		contains (x,y)

		Return:
		(bool): True if (x,y) is inside of rect, False otherwise.
		'''
		
		if x>=rect[0] and x<rect[0]+rect[2]\
				and y>=rect[1] and y<rect[1]+rect[3]:
			return True

	def load_image(self, rect, img_path):
		'''
		Display a selected picture in a certain position(x, y)
		The picture should be stored in asset folder

		Args:
		x, y(int): the coordinates where the picture should be displayed

		image_num(int): the name of the picture to be displayed
		'''

		# blit images to the subsurfaces
		image_load = pygame.image.load("asset/%s" % img_path)

		(x, y) = rect.center

		# in case no file is found
		if image_load == None:
			raise ValueError("No such file")

		self.screen.blit(image_load, (x-25, y-25, 0, 0)) 


	def display_current_playing(self):
		'''
		Displaying the score board while running the game
		'''
		text_surface = FONT.render(
			str(self.music_list[self.current_song_index]),
			True,
			pygame.Color("white"),
			pygame.Color("black"))
		self.screen.fill(pygame.Color("black"), self._rect_caption)
		self.screen.blit(text_surface, self._rect_caption)

	
	def on_click(self, x, y):
		'''
		Handles the functionality when the mouse is pressed on the
		 surface.
		'''

		# if mouse pressed on the surface for tiles
		if self.is_in_rect(x, y, self._rect_surface_tiles):
			pass

