from math import *
from numpy import random

class vect(tuple):
    # a simple wrap for 2d vectors
    def __add__(self, w): return vect(map(lambda x,y:x+y, self, w))
    def __sub__(self, w): return vect(map(lambda x,y:x-y, self, w))
    def __mul__(self, c): return vect(map(lambda x:x*c, self))
    def __div__(self, c): return vect(map(lambda x:x/c, self))
    def __neg__(self): return vect(map(lambda x:-x, self))
    def __iadd__(self, w): return self + w
    def __isub__(self, w): return self - w
    def __imul__(self, c): return self * c
    def __idiv__(self, c): return self / c
    def norm(self): return sqrt(sum(map(lambda x:x*x, self)))
    def __repr__(self): return 'vect('+str(self)+')'

vect.zero = vect((0.0,0.0))


random.seed(666)
C = 0.4

# graph generator
def graphs():
    graph = {0 : set([])}
    i = 0
    while True:
        yield graph
        i += 1
        # choose vertices to connect to:
        c = int(floor(C * sqrt(i)))
        graph[i] = set(random.choice(i, size = c, replace = False))
        for j in graph[i]:
            graph[j].add(i)

# def dfs(graph):
#     return _dfs(graph,0,set([0]))
#
# def _dfs(graph, cur, visited):
#     if len(visited) == len(graph):
#         return True
#     for i in (graph[cur] - visited):
#         if _dfs(graph, cur, visited|set([i])):
#             return True
#     return False

# for g in graphs():
#     print '*',
#     sys.stdout.flush()
#     if dfs(g): print len(g)
#     if len(g) == 5:
#         break
# print "done"
