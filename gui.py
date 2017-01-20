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
		#self.screen = pygame.display.set_mode(screen_size_tuple, pygame.FULLSCREEN)
		self.screen = pygame.display.set_mode(screen_size_tuple, 0,0)
		pygame.display.set_caption("Music")

		self._width = screen_size_tuple[0] #480
		self._height = screen_size_tuple[1] #320
		print(self._height, self._width)
		
		self._rect_screen = pygame.Rect(0, 0, self._width, self._height) # size of the window
		self._rect_menu = pygame.Rect(0, 0, self._width/4, self._height/4)
		self._rect_caption = pygame.Rect(self._width/4, 0, self._width/2, self._height/4)
		self._rect_mode = pygame.Rect((self._width*3)/4, 0, self._width/4, self._height/4)
		self._rect_controls = pygame.Rect(0, self._height/4, self._width, (self._height*3)/4)

		self._rect_rollback = pygame.Rect(0, self._height/4, self._width/4, (self._height*3)/4)

		self._rect_center = pygame.Rect(self._width/4, self._height/4, self._width/2, (self._height*3)/4)
		self._rect_vol_up = pygame.Rect(self._width/4, self._height/4, self._width/2, (self._height*3)/16)
		self._rect_pause = pygame.Rect(self._width/4, (self._height*7)/16, self._width/2, (self._height*3)/8)
		self._rect_vol_down = pygame.Rect(self._width/4, (self._height*13)/16, self._width/2, (self._height*3)/16)
		self._rect_forward = pygame.Rect((self._width*3)/4, self._height/4, self._width/4, (self._height*3)/4)

		self.init_player(path)


	def init_player(self, path):		
		self.play_status = 'playing'
		self.play_mode = -1
		self.music_list = self.music_setup(path)
		self.current_song_index = 0
		#self.screen.fill((122,122,122), self._rect_rollback)
		#self.screen.fill((122,122,122), self._rect_forward)
		#self.screen.fill((122,122,122), self._rect_vol_down)
		#self.screen.fill((122,122,122), self._rect_vol_up)

		print("songs/%s"%self.music_list[self.current_song_index])
		pygame.mixer.music.load("songs/%s"%self.music_list[self.current_song_index])

		pygame.mixer.music.play(self.play_mode, 0.0)
		#while pygame.mixer.music.get_busy(): 
		#	pygame.time.Clock().tick(10)

		print(self._rect_menu)
		print(self._rect_caption)
		print(self._rect_mode)
		print(self._rect_rollback)
		print(self._rect_pause)
		print(self._rect_forward)
		self.load_image(self._rect_rollback, "rollback1.png")
		self.load_image(self._rect_mode, "one.png")
		self.load_image(self._rect_menu, "menu.png")
		self.load_image(self._rect_pause, "pause1.png")
		self.load_image(self._rect_forward, "forward1.png")
		self.blit_text('VOL +', self._rect_vol_up)
		self.blit_text('VOL -', self._rect_vol_down)
	
	def blit_text(self, text, rect):
		text_surface = FONT.render(
			text,
			True,
			pygame.Color("white"),
			pygame.Color("black"))
		self.screen.fill(pygame.Color("black"), rect)
		self.screen.blit(text_surface, rect)

	def music_setup(self, path):
		songs = []
		output = []
		with open(path, 'r') as f:
			songs = f.readlines()
		for song in songs:
			output.append(song.strip())
		print(output)
		return output

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

	def fill_rect_color(self, rect, color):
		self.screen.fill(color, rect)

	def clear_rect(self, rect):
		self.fill_rect_color((255,255,255), rect)

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

	def update(self):
		self.display_current_playing()
	
	def on_click(self, x, y):
		'''
		Handles the functionality when the mouse is pressed on the
		 surface.
		'''

		# if mouse pressed on the surface for tiles
		if self.is_in_rect(x, y, self._rect_rollback):
			if self.current_song_index==0:
				self.current_song_index = len(self.music_list)-1
			else:
				self.current_song_index-=1

			print("songs/%s"%self.music_list[self.current_song_index])
			pygame.mixer.music.load("songs/%s"%self.music_list[self.current_song_index])
			pygame.mixer.music.play(self.play_mode, 0.0)
		elif self.is_in_rect(x, y, self._rect_pause):
			if self.play_status == 'playing':
				print(self.play_status)
				pygame.mixer.music.pause()
				self.screen.fill((0,0,0), self._rect_pause)
				self.load_image(self._rect_center, "start1.png")
				self.play_status = 'paused'
			else:
				print(self.play_status)
				pygame.mixer.music.unpause()
				self.screen.fill((0,0,0), self._rect_pause)
				self.load_image(self._rect_center, "pause1.png")
				self.play_status = 'playing'
		elif self.is_in_rect(x, y, self._rect_forward):
			if self.current_song_index==len(self.music_list)-1:
				print('length:', len(self.music_list))
				print(self.current_song_index)
				self.current_song_index = 0
			else:
				self.current_song_index+=1

			print("songs/%s"%self.music_list[self.current_song_index])
			pygame.mixer.music.load("songs/%s"%self.music_list[self.current_song_index])
			pygame.mixer.music.play(self.play_mode, 0.0)
		elif self.is_in_rect(x, y, self._rect_mode):
			if self.play_mode == -1:
				self.play_mode = 1
			elif self.play_mode == 1:
				self.play_mode = -1
		elif self.is_in_rect(x,y, self._rect_menu):
			pass
		else:
			pass
		



