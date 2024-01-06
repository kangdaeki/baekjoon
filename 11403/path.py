# to speed up the slow input()
import sys
from collections import deque

input = sys.stdin.readline
N=int(input())
dist=[]
for _ in range(N):
    dist.append(list(map(int,input().split())))
for k in range(N):
    for i in range(N):
        for j in range(N):
            if 1==dist[i][k] and 1==dist[k][j]: dist[i][j]=1
for i in range(N):
    for j in range(N):
       print(dist[i][j],end=" ")
    print()
