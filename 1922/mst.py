import sys
input=sys.stdin.readline
V=int(input())
E=int(input())
#MAKE-SET
p=[x for x in range(V+1)]

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

from queue import PriorityQueue
que=PriorityQueue()

for _ in range(E):
    u,v,w=map(int,input().split())
    que.put((w,u,v))

cost=0
for _ in range(E):
    w,u,v=que.get()
    if not is_same(u,v):
        cost+=w
        union(u,v)
print(cost)
