import sys
input=sys.stdin.readline
V,E=map(int,input().split())
K=int(input())
distance=[sys.maxsize]*(V+1)
visited=[False]*(V+1)
graph=[[] for _ in range(V+1)]
from queue import PriorityQueue
q=PriorityQueue()
for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
q.put((0,K))
distance[K]=0
while q:
    current=q.get()
    c_v=current[1]
    if visited[c_v]: continue
    visited[c_v]=True
    for v,w in graph[c_v]:
        if distance[v]>distance[c_v]+w:
            distance[v]=distance[c_v]+w
            q.put((distance[v],v))
for i in range(1,V+1):
    if visited[i]:
        print(dist[i])
    else:
        print("INF")
