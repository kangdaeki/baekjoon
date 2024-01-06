import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
import collections
graph=collections.defaultdict(list)
for _ in range(M):
    s,t,c=map(int,input().split())
    graph[s].append((t,c))
S,T=map(int,input().split())
Q=[(0,S)]
dist=collections.defaultdict(int)
import heapq
while Q:
    time,node=heapq.heappop(Q)
    if node not in dist:
        dist[node]=time
        for v,w in graph[node]:
            alt=time+w
            heapq.heappush(Q,(alt,v))
print(dist[T])
