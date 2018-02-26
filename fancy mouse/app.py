import sys, pygame
from math import *

# expected size of the window
size = width, height = 600, 400

class color:
    red = 250, 50, 50
    violet = 238,130,238
    lgreen = 0, 250, 0
    black = 0, 0, 0
    gray = 100,100,100
    lgray = 210,210,210
    white = 250,250,250

maze_layer = [[0]*height for _ in range(width)]

def draw_maze():
    screen.fill(color.white)
    screen.fill(color.white)
    for i in range(width):
        for j in range(height):
            if maze_layer[i][j]:
                # set color of the pixel (i,j) to black
                pass

pygame.init()
screen = pygame.display.set_mode(size)

while 1:

    draw_maze()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if even.type == pygame.MOUSEMOTION:
            pass
