import pygame
#from pygame import *
#import pygame.mixer.music as music

def main():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load("test.mp3")
	pygame.mixer.music.play(-1, 0.0)

if __name__ == '__main__':
	main()