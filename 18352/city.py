# to speed up the slow input()
import sys
input = sys.stdin.readline
N,M,K,X=map(int,input().split())
graph=dict()
for _ in range(M):
    u,v=map(int,input().split())
    if u not in graph: graph[u]={v}
    else: graph[u].add(v)
visited=[False for _ in range(N+1)]
from collections import deque
deq=deque()
deq.append((X,0))
visited[X]=True
result=[]
while deq:
    u,d=deq.popleft()
    if d==K: result.append(u)
    if d>K: break
    if u in graph:
        for v in graph[u]:
            if not visited[v]:
                visited[v]=True
                deq.append((v,d+1))
if 0==len(result): print(-1)
else: 
    result.sort()
    for node in result: print(node)
