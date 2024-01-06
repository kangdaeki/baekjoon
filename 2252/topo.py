# to speed up the slow input()
import sys
input = sys.stdin.readline
N,M=map(int,input().split())
visited=[False for _ in range(N)]
degree=[0 for _ in range(N)]
graph=dict()
for i in range(M):
    u,v=map(int,input().split())
    if u in graph: graph[u].add(v)
    else: graph[u]={v}
    degree[v-1]+=1
from collections import deque
deq=deque()
for i in range(N):
    if 0==degree[i]: deq.append(i)
while deq:
    i=deq.popleft()
    visited[i]=True
    print(i+1,end=" ")
    if i+1 in graph:
        for v in graph[i+1]:
            degree[v-1]-=1
            if 0==degree[v-1]: deq.append(v-1)
