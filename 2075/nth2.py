import sys
input=sys.stdin.readline
N=int(input())
import heapq
hq=[]
for i in range(N):
    line=list(map(int,input().split()))
    if 0==i:
        for j in range(N): 
            heapq.heappush(hq, line[j])
    else:
        for j in range(N): 
            heapq.heappushpop(hq, line[j])
print(hq[0])


