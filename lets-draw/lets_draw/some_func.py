import math
import pygame
from default_colors import *
from const import *
def slash(surf, d, pos, l):
    color = GRAY
    dx = d[0]
    dy = d[1]
    if dx == 0:
        color = L_GREEN
    else:
        tg = dy/dx
        if tg>0.5:
            color = L_GREEN
        if tg<-0.5:
            color = L_RED
        if tg>2.5:
            color = GREEN
        if tg<-2.5:
            color = RED
    #dx, dy = float(l), float(l)*tg
    de = l/math.sqrt(dx*dx+dy*dy)
    dx*=de
    dy*=de
    dx = int(dx)
    dy = int(dy)
    rect = surf.get_rect()
    w,h = rect.width/2, rect.height/2
    pygame.draw.line(surf, color, (pos[0]+w-dx, h-pos[1]+dy), (pos[0]+w+dx, h-pos[1]-dy), 1)
def dr_func(surf, func, color):
    rect = surf.get_rect()
    w,h = rect.width/2, rect.height/2
    pix_arr = pygame.PixelArray(surf)
    for i in range(rect.width):
        for j in range(rect.height):
            if func(i-w,h-j)==0:
                pix_arr[i][j]=color
    del pix_arr
def norm(w):
    wx,wy = w[0],w[1]
    l = math.sqrt(wx*wx+wy*wy)
    coef = 1
    if l!=0:
        coef = 1/math.sqrt(wx*wx+wy*wy)
    res = [w[0]*coef,w[1]*coef]
    return res
def dr_sol(surf, func, color, start):
    x, y = float(start[0]), float(start[1])
    rect = surf.get_rect()
    w,h = rect.width/2, rect.height/2
    pix_arr = pygame.PixelArray(surf)
    for i in range(5000):
        if(x>-w and x<w and y>-h and y<h):
            pix_arr[int(x)+w][h-int(y)]=color
        else:
            break
        dx,dy = norm(func(x,y))
        x+=dx
        y+=dy
        #tg = func(x,y)
        #if tg>2:
        #    x+=1/tg
        #    y+=1
        #elif tg<-2:
        #    x+=-1/tg
        #    y-=1
        #else:
        #    x+=0.5
        #    y+=0.5*tg
    x, y = float(start[0]), float(start[1])
    for i in range(0):
        if(x>-w and x<w and y>-h and y<h):
            pix_arr[int(x)+w][h-int(y)]=color
        else:
            break
        dx,dy = norm(func(x,y))
        x-=dx
        y-=dy
        #tg = func(x,y)
        #if tg>2:
        #    x-=1/tg
        #    y-=1
        #elif tg<-2:
        #    x-=-1/tg
        #    y+=1
        #else:
        #    x-=0.5
        #    y-=0.5*tg
    del pix_arr
def makeXgrid(surf, step, size, color = BLACK):
    rect = surf.get_rect()
    w,h = rect.width/2, rect.height/2
    x = w
    st = 0
    while x<=2*w:
        pygame.draw.line(surf, color, (x, H/2+size), (x, H/2-size), 1)
        st+=step
        x = w+int(st*SCALE)
    st = 0
    while x>=0:
        pygame.draw.line(surf, color, (x, H/2+size), (x, H/2-size), 1)
        st-=step
        x = w+int(st*SCALE)
def makeYgrid(surf, step, size, color = BLACK):
    rect = surf.get_rect()
    w,h = rect.width/2, rect.height/2
    y = h
    st = 0
    while y<=2*h:
        pygame.draw.line(surf, color, (W/2+size, y), (W/2-size, y), 1)
        st+=step
        y = h+int(st*SCALE)
    st = 0
    while y>=0:
        pygame.draw.line(surf, color, (W/2+size, y), (W/2-size, y), 1)
        st-=step
        y = h+int(st*SCALE)
    
    
