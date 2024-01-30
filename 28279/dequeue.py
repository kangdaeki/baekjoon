import sys
input=sys.stdin.readline
N=int(input())
from collections import deque
dq=deque()
for _ in range(N):
    l=list(input().split())
    if '1'==l[0]:
        dq.appendleft(int(l[1]))
    elif '2'==l[0]:
        dq.append(int(l[1]))
    elif '3'==l[0]:
        if 0==len(dq): print(-1)
        else: print(dq.popleft())
    elif '4'==l[0]:
        if 0==len(dq): print(-1)
        else: print(dq.pop())
    elif '5'==l[0]:
        print(len(dq))
    elif '6'==l[0]:
        if 0==len(dq): print(1)
        else: print(0)
    elif '7'==l[0]:
        if 0==len(dq): print(-1)
        else: print(dq[0])
    elif '8'==l[0]:
        if 0==len(dq): print(-1)
        else: print(dq[-1])
