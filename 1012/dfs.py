import sys

def dfs(x,y):
    graph[y][x]=0
    if 0<y and 1==graph[y-1][x]: dfs(x,y-1)
    if N-1>y and 1==graph[y+1][x]: dfs(x,y+1)
    if 0<x and 1==graph[y][x-1]: dfs(x-1,y)
    if M-1>x and 1==graph[y][x+1]: dfs(x+1,y)

T=int(input())
sys.setrecursionlimit(10000)   
for _ in range(T):
    M,N,K=map(int,input().split())
    graph=[[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x,y=map(int,input().split())
        graph[y][x]=1
    count=0
    for y in range(N):
        for x in range(M):
            if 1==graph[y][x]:
                count+=1
                dfs(x,y)
    print(count)


