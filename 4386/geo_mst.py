import sys
input=sys.stdin.readline
n=int(input())
coord=[]
for i in range(n):
    x,y=map(float,input().split())
    coord.append((x,y,i+1))
import itertools
import math
from queue import PriorityQueue
que=PriorityQueue()
E=0
for (x1,y1,u),(x2,y2,v) in  itertools.combinations(coord,2):
    d=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
    que.put((d,u,v))
    E+=1

#MAKE-SET
p=[x for x in range(n+1)]

#FIND-SET
def find_set(x):
    if p[x]!=x: p[x]=find_set(p[x])
    return p[x]

#UNION
def union(x,y):
    p[find_set(y)]=find_set(x)

#IS-SAME
def is_same(x,y):
    return find_set(x)==find_set(y)

cost=0
for _ in range(E):
    w,u,v=que.get()
    if not is_same(u,v):
        cost+=w
        union(u,v)
print(cost)
