import sys
import pygame
from math import *
from numpy import random
from mymath import graphs, vect

# expected size of the window
size = width, height = 600, 400

################################################################################
# drawing manager
################################################################################
class color:
    red = 250, 50, 50
    violet = 238,130,238
    lgreen = 0, 250, 0
    black = 0, 0, 0
    gray = 100,100,100
    lgray = 210,210,210
    white = 250,250,250


def draw(g):
    layout = lm.layout(width, height)
    def vertex(v):
        pos = layout[v]
        pygame.draw.circle(screen, color.black, pos, 3)
        # dx = vect([10,0])
        # dy = vect([0,10])
        # pygame.draw.line(screen, color.black, pos-dx, pos+dx)
        # pygame.draw.line(screen, color.black, pos-dy, pos+dy)
    def edge(v,w):
        pv = layout[v]
        pw = layout[w]
        pygame.draw.aaline(screen, color.gray, pv, pw)
    # draw vertices
    for v in g:
        vertex(v)
    # draw lines
    for v in g:
        for w in g[v]:
            if v < w: edge(v,w)

def draw_forces(g,f, c):
    layout = lm.layout(width, height)
    forces = lm.forces(width, height, f)
    for v in g:
        pv = layout[v]
        pw = layout[v]+forces[v]
        pygame.draw.aaline(screen, c, pv, pw)

def draw_grid():
    xs,ys = lm.grid(width, height)
    c = color.lgray
    for x in xs:
        for y in ys:
            pygame.draw.line(screen, c, (x-2,y), (x+2,y))
            pygame.draw.line(screen, c, (x,y-2), (x,y+2))

################################################################################
# physics engine
################################################################################
class physics:
    # iterations = 100
    # delta = 0.3
    eps = 0.0001
    @staticmethod
    def max_force():
        return 10.0
        # return max(lm.width, lm.height) / 5
    dt = 0.01
    iterations = 100

    @staticmethod
    def charge(v,w): # charge based repulsive force between pos v and pos w
        r = v - w
        d = r.norm()
        if d < physics.eps: d = physics.eps # points are too close
        f = 1.0/d*d*d
        re =  r * f
        if re.norm() > physics.max_force():
            re *= physics.max_force()/re.norm()
        return re

    @staticmethod
    def stretch(v,w): # stretch-based force between pos v and w
        r = v - w
        d = r.norm()
        re = -r
        # this caused troubles, do not uncomment!
        # if re.norm() > physics.max_force():
        #     re *= physics.max_force()/re.norm()
        return re

    @staticmethod
    def charges(g):
        f = {}
        for v in g:
            f[v] = vect.zero
            for w in g:
                if v == w: continue
                f[v] += physics.charge(points[v], points[w])
        return f

    @staticmethod
    def stretches(g):
        f = {}
        for v in g:
            f[v] = vect.zero
            for w in g[v]:
                f[v] += physics.stretch(points[v], points[w])
            # add gravity to center so that vertices do not run away
        return f

    @staticmethod
    def central(g):
        f = {}
        for v in g:
            f[v] = vect.zero
            f[v] += physics.stretch(points[v], vect.zero) * 2
        return f

    @staticmethod
    def move_one_step(g):
        ch = physics.charges(g)
        st = physics.stretches(g)
        ce = physics.central(g)
        for v in points:
            dp = (ch[v]+st[v]+ce[v]) * physics.dt
            # if dp.norm() > physics.max_force():
            #     dp *= physics.max_force()/dp.norm()
            points[v] += dp
#     def move(): #moves vertices many times
#         for t in range(T):
#             move_one_step()
#

################################################################################
# layout, just contains all the coordinates for points in the graph
################################################################################
points = {0:vect.zero}
################################################################################
# layout manager
################################################################################

class lm:
    margin = 0.5

    # sets the border to include all the points
    @classmethod
    def set_border(cls):
        dots = points.values()
        x = map(lambda d: d[0], dots)
        y = map(lambda d: d[1], dots)
        cls.left, cls.right = min(x)-lm.margin, max(x)+lm.margin
        cls.top, cls.bot = min(y)-lm.margin, max(y)+lm.margin
        cls.width = cls.right - cls.left
        cls.height = cls.bot - cls.top

    # return absolute values for positioning points on the screen
    @staticmethod
    def layout(w,h):
        lm.set_border()
        re = {}
        for v in points:
            p = points[v]
            x = p[0]-lm.left
            y = p[1]-lm.top
            re[v] = vect( (int(x/lm.width*w), \
                           int(y/lm.height*h)) )
        return re

    # adds a new point to points and assigns it a random position
    @staticmethod
    def add_new_vertex():
        while 1:
            x = lm.left + random.random() * lm.width
            y = lm.top + random.random() * lm.height
            new_dot = vect([x, y])
            #make sure we do not
            if new_dot not in points.values(): break
        points[len(points)] = new_dot
        lm.set_border()

    @staticmethod
    def forces(w,h,f):
        re = {}
        for v in f:
            re[v] = vect( (int(f[v][0]/lm.width*w), \
                           int(f[v][1]/lm.height*h)) )
        return re

    @staticmethod
    def grid(w,h):
        def step(l):
            i = 1
            while l / i > 20:
                i *= 10
            return i
        xstep = step(lm.width)
        ystep = step(lm.height)
        x = 0.0
        while x - xstep > lm.left:
            x -= xstep
        xs = []
        while x < lm.right:
            xs.append(int( (x-lm.left) / lm.width * w ))
            x += xstep
        y = 0.0
        while y - ystep > lm.top:
            y -= ystep
        ys = []
        while y < lm.bot:
            ys.append(int( (y-lm.top) / lm.height * h ))
            y += ystep
        return xs,ys
gi = graphs()
g = gi.next()
# init some other shit?

pygame.init()

screen = pygame.display.set_mode(size)

screen.fill(color.white)
draw(g)
pygame.display.flip()

while 1:
    screen.fill(color.white)
    draw_grid()
    draw(g)
    # draw_forces(g, physics.charges(g), color.red)
    # draw_forces(g, physics.stretches(g), color.lgreen)
    # draw_forces(g, physics.central(g), color.violet)
    pygame.display.flip()
    physics.move_one_step(g)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==pygame.KEYUP:
            # add new vertex, move some shit, redraw
            g = gi.next()
            lm.add_new_vertex()
            # screen.fill(color.white)
            # draw(g)
            # pygame.display.flip()
