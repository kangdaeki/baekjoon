import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
import collections
graph=collections.defaultdict(list)
for _ in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
Q=[(0,0,1)]
dist=collections.defaultdict(int)
import heapq
while Q:
    time,count,node=heapq.heappop(Q)
    print(time,count,node)
    if count>k:
        break
    dist[node]=time
    for v,w in graph[node]:
        alt=time+w
        heapq.heappush(Q,(alt,count+1,v))
    """
    if node not in dist:
        print(time,count,node)
        dist[node]=time
        for v,w in graph[node]:
            alt=time+w
            heapq.heappush(Q,(alt,count+1,v))
    """
print(dist)
