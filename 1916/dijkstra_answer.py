import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)]
dist=[sys.maxsize]*(N+1)
visited=[False]*(N+1)
for _ in range(M):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
S,E=map(int,input().split())

from queue import PriorityQueue
def dijkstra(s,e):
    Q=PriorityQueue()
    Q.put((0,s))
    dist[s]=0
    while Q.qsize()>0:
        d,u=Q.get()
        if not visited[u]:
            visited[u]=True
            for v,w in graph[u]:
                if not visited[v] and dist[v]>dist[u]+w:
                    dist[v]=dist[u]+w
                    Q.put((dist[v],v))
    return dist[e]

print(dijkstra(S,E))

