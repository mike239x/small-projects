import sys, pygame
from math import *

# expected size of the window
size = width, height = 600, 400 #600, 400

class color:
    red = 250, 50, 50
    violet = 238,130,238
    lgreen = 0, 250, 0
    black = 0, 0, 0
    gray = 100,100,100
    lgray = 210,210,210
    white = 250,250,250

maze_layer = {}

def draw_maze(s):
    # pixObj = pygame.PixelArray(s)
    screen.fill(color.white)
    for pos in maze_layer:
        pygame.draw.line(s, color.black, pos, pos)
        #i,j = pos
        # pixObj[i][j] = color.black
        # set color of the pixel (i,j) to black
    # del pixObj

pygame.init()
screen = pygame.display.set_mode(size)
cursor_size = 15 # pix

def on_screen(x,y):
    return x in range(width) and y in range(height)

def maze_iter():
    delete = {}
    for pos in maze_layer:
        i,j = pos
        n = 0 # neightbors
        for di in range(-1,2):
            for dj in range(-1,2):
                if (i+di,j+dj) in maze_layer:
                    n += 1
        if n < 6:
            delete[pos] = True
    for pos in delete:
        del maze_layer[pos]

def draw_circle(x,y):
    c = cursor_size
    for dx in range(-c, c+1):
        for dy in range(-c,c+1):
            if dx*dx+dy*dy > c*c: continue
            px = x+dx
            py = y+dy
            if not on_screen(px,py): continue
            maze_layer[px,py] = 1

while 1:
    draw_maze(screen)
    maze_iter()
    pygame.display.flip()
    # print('step')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if pygame.key.name(event.key) == 'c':
                maze_layer.clear()
            else:
                print(maze_layer)
        if event.type == pygame.MOUSEMOTION:
            x,y = event.pos
            draw_circle(x,y)
            # pygame.display.flip()
