# to speed up the slow input()
import sys
input = sys.stdin.readline
N,M=map(int,input().split())
if 0==N:
    print(0)
    exit()
if 1==N:
    print(1)
    exit()
graph={}
for i in range(1,N+1):
    graph[i]=set()
for _ in range(M):
    u,v=map(int,input().split())
    graph[u].add(v) 
    graph[v].add(u) 

visited=[False for _ in range(N+1)]
all_visited=False

from collections import deque
deq=deque()
cc=0
while not all_visited:
    for i in range(1,N+1):
        if not visited[i]:
            visited[i]=True
            deq.append(i)
            while deq:
                j=deq.popleft()
                for k in graph[j]:
                    if not visited[k]:
                        visited[k]=True
                        deq.append(k)
            cc+=1

    all_visited=True
    for i in range(1,N+1):
        if not visited[i]:
            all_visited=False
            break

print(cc)
