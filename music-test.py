import sys, pygame, os, gui, time
import asset
from gui import GUI
#from modegui import ModeWindow

# define the position for generating the windows
# from pygame wiki
#X = 150
#Y = 50
#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X, Y)
SCREEN_SIZE = (480,320)
LOCAL_PATH = "song_list.txt"

def main():
	# add background music to the game
	pygame.init()
	#pygame.mixer.init()
	#pygame.mixer.music.load("test.mp3")
	#pygame.mixer.music.play(-1, 0.0)

	# initialize the surface
	surface = GUI(SCREEN_SIZE, LOCAL_PATH)

	while True:

		# update the surface and all objects
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.display.quit()
				sys.exit()
			# End if q is pressed
			elif (event.type == pygame.KEYDOWN and
			(event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
				pygame.display.quit()
				sys.exit()
			# Respond to clicks
			elif event.type == pygame.MOUSEBUTTONUP:
				mouse_pos = event.pos
				x_mouse = mouse_pos[0]
				y_mouse = mouse_pos[1]
				surface.on_click(x_mouse, y_mouse)
				pygame.display.update()

	# display the ending pictures to the player
	print("game over")

	sys.exit()

if __name__ == '__main__':
	main()

