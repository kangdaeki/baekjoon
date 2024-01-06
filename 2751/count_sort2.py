# to speed up the slow input()
import sys
input = sys.stdin.readline
N=int(input())
pos_data=[False for _ in range(1_000_000+1)]
neg_data=[False for _ in range(1_000_000+1)]
for _ in range(N):
    n=int(input())
    if n>=0:
        pos_data[n]=True
    else:
        neg_data[-n]=True
for i in range(1_000_000,0,-1):
    if neg_data[i]: print(-i)
for i in range(1_000_000+1):
    if pos_data[i]: print(i)

