import sys
input=sys.stdin.readline
from queue import PriorityQueue
while True:
    N=int(input())
    if -1==N:
        break
    q=PriorityQueue()
    sum=1
    import math
    for i in range(2,1+int(math.sqrt(N))):
        if 0==N%i:
            q.put(i)
            q.put(N//i)
            sum+=i+N//i
    if N!=sum:
        print(N,'is NOT perfect.')
    else:
        print(N,'= 1',end='')
        while q.qsize()>0:
            print(' +',q.get(), end='')
        print()
