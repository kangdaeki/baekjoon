import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
M=int(input())
C=list(map(int,input().split()))
from collections import deque
dq = deque()
for i in range(N-1,-1,-1): 
    if 0==A[i]: dq.append(B[i])
for i in range(M-len(dq)): dq.append(C[i])
for i in range(M): print(dq.popleft(),end=' ')
print()
