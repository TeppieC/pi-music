import pygame, sys, os
from pygame import time
#from pygame import *
#import pygame.mixer.music as music

'''
def main():
        pygame.init()
        pygame.mixer.init()
        pygame.time.delay(1000)
        #pygame.mixer.music.load("test.mp3")
        pygame.mixer.music.load("classical_music.mp3")
        pygame.mixer.music.play(-1, 0.0)

if __name__ == '__main__':
        main()
'''


# define the position for generating the windows
# from pygame wiki
X = 150
Y = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X, Y)

pygame.init()
pygame.mixer.init()
pygame.time.delay(1000)
pygame.mixer.music.load("test.mp3")
#pygame.mixer.music.load("classical_music.mp3")
pygame.mixer.music.play(-1, 0.0)

#wait for strat
while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
