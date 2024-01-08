import sys
input=sys.stdin.readline
V,E=map(int,input().split())
K=int(input())
import collections
graph=collections.defaultdict(list)
#graph=[[] for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
Q=[(0,K)]
dist=collections.defaultdict(int)
#dist={}
import heapq
while Q:
    time,node=heapq.heappop(Q)
    if node not in dist:
        dist[node]=time
        for v,w in graph[node]:
            alt=time+w
            heapq.heappush(Q,(alt,v))
for i in range(1,V+1):
    if i in dist:
        print(dist[i])
    else:
        print("INF")
