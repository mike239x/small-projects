# -*- coding: cp1251 -*-
import pygame, sys
from pygame.locals import *
from default_colors import *
from some_func import *
from const import *
pygame.init()

pygame.display.set_caption('Draw it, dummy Mike!')
DISPLAYSURF = pygame.display.set_mode((W, H))
DISPLAYSURF.fill(WHITE)
def der_(x,y):
    if (2*x-y*y)!=0:
        return x/(2*x-y*y)
    return 1000000
def deriv(x_,y_):
    x,y = float(x_)/SCALE, float(y_)/SCALE
    return der_(x,y)
def zero_izokl (x_,y_):
    # x - 1/2 y^2
    x,y = float(x_)/SCALE, float(y_)/SCALE
    re = 2*x*x - y*x*2 + y*y*y
    if re<0:
        re = -re
    if re < 0.015:
        return 0
    else:
        return 1
def liniya_peregibov(x_,y_):
        # x - 1/2 y^2
    x,y = float(x_)/SCALE, float(y_)/SCALE
    re = der_(x,y)
    if re<0:
        re = -re
    if re < 0.003:
        return 0
    else:
        return 1    
#поле направлений
x,y = -W/2+2, -H/2+2
for i in range(H/10):
    for j in range(W/10):
        slash(DISPLAYSURF, deriv(x,y), (x,y), 5)
        x+=10
    y+=10
    x =-W/2+2
#stage 1:
dr_func(DISPLAYSURF, zero_izokl, DARK_GRAY)
dr_func(DISPLAYSURF, liniya_peregibov, BLACK)
#stage 2: some solutions
#part a: on the left:
dr_sol(DISPLAYSURF, deriv, BLUE, (-5,80))
#dr_sol(DISPLAYSURF, deriv, BLUE, (-75,200))
dr_sol(DISPLAYSURF, deriv, BLUE, (-75,0))
#dr_sol(DISPLAYSURF, deriv, BLUE, (-150,0))
dr_sol(DISPLAYSURF, deriv, BLUE, (-225,0))
#dr_sol(DISPLAYSURF, deriv, BLUE, (-300,0))
dr_sol(DISPLAYSURF, deriv, BLUE, (-300,-100))
#dr_sol(DISPLAYSURF, deriv, BLUE, (-300,-200))
#part b: on the right:
dr_sol(DISPLAYSURF, deriv, BLUE, (75,0))
#dr_sol(DISPLAYSURF, deriv, BLUE, (150,0))
dr_sol(DISPLAYSURF, deriv, BLUE, (225,0))
#dr_sol(DISPLAYSURF, deriv, BLUE, (300,0))
dr_sol(DISPLAYSURF, deriv, BLUE, (375,0))
#dr_sol(DISPLAYSURF, deriv, BLUE, (375,75))
dr_sol(DISPLAYSURF, deriv, BLUE, (375,150))
#dr_sol(DISPLAYSURF, deriv, BLUE, (375,225))
dr_sol(DISPLAYSURF, deriv, BLUE, (110,-110))
#dr_sol(DISPLAYSURF, deriv, BLUE, (110,-160))
dr_sol(DISPLAYSURF, deriv, BLUE, (110,-240))
#part 3: on the right top:
dr_sol(DISPLAYSURF, deriv, BLUE, (5,150))
#dr_sol(DISPLAYSURF, deriv, BLUE, (50,200))
dr_sol(DISPLAYSURF, deriv, BLUE, (100,200))
#сепаратриссы:
#dr_sol(DISPLAYSURF, deriv, ORANGE, (-1,-1))
#dr_sol(DISPLAYSURF, deriv, ORANGE, (1,-1))
#dr_sol(DISPLAYSURF, deriv, ORANGE, (265,249))
dr_sol(DISPLAYSURF, deriv, BLUE, (0,-50))
dr_sol(DISPLAYSURF, deriv, BLUE, (0,-100))
dr_sol(DISPLAYSURF, deriv, BLUE, (0,-150))
dr_sol(DISPLAYSURF, deriv, BLUE, (0,-200))

#coords:
pygame.draw.line(DISPLAYSURF, BLACK, (0,H/2), (W, H/2), 2)
pygame.draw.line(DISPLAYSURF, BLACK, (W/2,0), (W/2, H), 1)
#x-coords:
makeXgrid(DISPLAYSURF, 0.25, 2)
makeXgrid(DISPLAYSURF, 0.5, 4)
makeXgrid(DISPLAYSURF, 1, 6)
#y-coords:
makeYgrid(DISPLAYSURF, 0.25, 2)
makeYgrid(DISPLAYSURF, 0.5, 4)
makeYgrid(DISPLAYSURF, 1, 6)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit('bye-bye')
    pygame.display.update()

