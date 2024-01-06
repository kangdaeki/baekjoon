import sys
from collections import deque

def DFS(s):
    if not visited[s]:
        visited[s]=True
        print(s, end=" ")
        for c in graph[s]:
            DFS(c)

def BFS(s):
    visited[s]=True
    print(s, end=" ")
    deq=deque()
    deq.append(s)
    while deq:
        p=deq.popleft()
        for c in graph[p]:
            if not visited[c]:
                visited[c]=True
                print(c, end=" ")
                deq.append(c)

# to speed up the slow input()
input = sys.stdin.readline
N,M,V=map(int,input().split())

graph={}
for i in range(1,N+1):
    graph[i]=[]

for _ in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort()

visited=[False for _ in range(N+1)]
DFS(V)
print()
visited=[False for _ in range(N+1)]
BFS(V)
print()
