import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
import collections
graph=collections.defaultdict(list)
for _ in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
dist=[[sys.maxsize for _ in range(k)] for _ in range(n+1)]
dist[1][0]=0 # (node,K)
Q=[(0,1)] # (weight=cost,node)
import heapq
while Q:
    cost,node=heapq.heappop(Q)
    for v,w in graph[node]:
        alt=cost+w
        if dist[v][k-1]>alt:
            dist[v][k-1]=alt
            dist[v].sort()
            heapq.heappush(Q,(alt,v))
for i in range(1,n+1):
    if sys.maxsize==dist[i][k-1]: print(-1)
    else: print(dist[i][k-1])
