def next(q,i,N):
    i+=1
    if i>=N: i=0
    if 0==q[i]: i=next(q,i,N)
    return i

def prev(q,i,N):
    i-=1
    if i<0: i=N-1
    if 0==q[i]: i=prev(q,i,N)
    return i

import sys
input=sys.stdin.readline
N=int(input())
q=list(map(int,input().split()))
i=0
for _ in range(N-1):
    print(i+1,end=' ')
    n=q[i]
    q[i]=0
    if 0<n:
        for _ in range(n):  i=next(q,i,N)
    elif 0>n:
        for _ in range(-n):  i=prev(q,i,N)
print(i+1)
