import sys
input=sys.stdin.readline

def union(x,y):
    a=find_set(x)
    b=find_set(y)
    if a!=b:
        p[a]=b
    return

def find_set(x):
    r=x
    while r!=p[r]:
        r=p[r]
    # path compression
    while x!=p[x]:
        y=p[x]
        p[x]=r
        x=y
    return r

N,Q=map(int,input().split())
v=[i for i in range(N+1)]
for i in range(2,N+1):
    v[i]=int(input())

from collections import deque
deq=deque()
for i in range(N+Q-1):
    line=input()
    if '0'==line[0]:
        x,b=map(int,line.split())
        deq.append((x,b))
    else:
        x,c,d=map(int,line.split())
        deq.append((x,c,d))

p=[i for i in range(N+1)]
ans=[]
while deq:
    q=deq.pop()
    if 0==q[0]:
        union(q[1], v[q[1]])
    else:
        a=find_set(q[1])
        b=find_set(q[2])
        if a==b:
            ans.append("YES")
        else:
            ans.append("NO")

print(*ans[::-1],sep='\n')

