import sys
input=sys.stdin.readline
from queue import PriorityQueue
N,K=map(int,input().split())
q=PriorityQueue()
q.put(1)
q.put(N)
import math
for i in range(2,1+int(math.sqrt(N))):
    if 0==N%i:
        q.put(i)
        if i!=(N//i):
            q.put(N//i)
if K>q.qsize():
    print(0)
else:
    for _ in range(K-1):
        q.get()
    print(q.get())
