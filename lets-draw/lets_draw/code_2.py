# -*- coding: cp1251 -*-
import pygame, sys
from pygame.locals import *
from default_colors import *
from some_func import *
from const import *
from math import *
from random import randint
pygame.init()

k = randint(1,3)*2+1
a = randint(-3,3)
b = randint(1,3)
c = randint(-3,3)
d = randint(1,3)
if b*c < 0:
    b=-b
if a*d > 0:
    a=-a
pygame.display.set_caption("Draw it, dummy Mike! x' = "+str(a)+"x^3"+(str(b) if b<0 else "+"+str(b))+"y^"+str(k)+"; y' = "+str(c)+"x"+(str(d) if d<0 else "+"+str(d))+"y^"+str(k))
DISPLAYSURF = pygame.display.set_mode((W, H))
DISPLAYSURF.fill(WHITE)
def der_(x,y):
    dx = -1*pow(x,3)-1*pow(y,k)
    #r = abs(3*exp(y)-2*cos(x))
    #if r!=0:
    #    dx = log(r)
    #r = 8+12*y
    dy = 1*x+1*pow(y,k)
    #if r > 0:
    #    dy=-pow(8+12*y,float(1)/float(3))
    #else:
    #    dy=+pow(-8-12*y,float(1)/float(3))
    return [dx,dy]
def deriv(x_,y_):
    x,y = float(x_)/SCALE, float(y_)/SCALE
    return der_(x,y)
def zero_izokl (x_,y_):
    # x - 1/2 y^2
    dx,dy = deriv(x_,y_)
    re = dy
    if re<0:
        re = -re
    if re < DELTA:
        return 0
    else:
        return 1
def inf_izokl (x_,y_):
    # x - 1/2 y^2
    dx,dy = deriv(x_,y_)
    re = dx
    if re<0:
        re = -re
    if re < DELTA:
        return 0
    else:
        return 1
#def liniya_peregibov(x_,y_):
        # x - 1/2 y^2
#    x,y = float(x_)/SCALE, float(y_)/SCALE
#    re = x - y*y*2+y/2
#    if re<0:
#        re = -re
#    if re < 0.003:
#        return 0
#    else:
#        return 1    


#поле направлений
x,y = -W/2+2, -H/2+2
for i in range(H/10):
    for j in range(W/10):
        slash(DISPLAYSURF, deriv(x,y), (x,y), 5)
        x+=10
    y+=10
    x =-W/2+2
#stage 1:

#dr_func(DISPLAYSURF, zero_izokl, DARK_GRAY)
#dr_func(DISPLAYSURF, inf_izokl, DARK_GREEN)

#dr_func(DISPLAYSURF, liniya_peregibov, BLACK)

dr_sol(DISPLAYSURF, deriv, BLUE, (-100,1))
dr_sol(DISPLAYSURF, deriv, BLUE, (100,1))
dr_sol(DISPLAYSURF, deriv, BLUE, (1,100))
dr_sol(DISPLAYSURF, deriv, BLUE, (-1,-100))


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

