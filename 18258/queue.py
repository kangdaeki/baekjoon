import sys
input=sys.stdin.readline
N=int(input())
from collections import deque
dq=deque()
for _ in range(N):
    l=list(input().split())
    if 'push'==l[0]:
        dq.append(int(l[1]))
    elif 'pop'==l[0]:
        if 0==len(dq): print(-1)
        else: print(dq.popleft())
    elif 'size'==l[0]:
        print(len(dq))
    elif 'empty'==l[0]:
        if 0==len(dq): print(1)
        else: print(0)
    elif 'front'==l[0]:
        if 0==len(dq): print(-1)
        else: print(dq[0])
    elif 'back'==l[0]:
        if 0==len(dq): print(-1)
        else: print(dq[len(dq)-1])
