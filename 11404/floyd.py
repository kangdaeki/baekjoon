import sys
input=sys.stdin.readline
n=int(input())
max_d=2e9
d=[[max_d for _ in range(n)] for _ in range(n)]
for i in range(n):
    d[i][i]=0
m=int(input())
for _ in range(m):
    u,v,w=map(int,input().split())
    if d[u-1][v-1]>w: d[u-1][v-1]=w
for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j]>d[i][k]+d[k][j]:
                d[i][j]=d[i][k]+d[k][j]
for i in range(n):
    for j in range(n):
        if max_d==d[i][j]: print(0, end=" ")
        else: print(d[i][j],end=" ")
    print()
