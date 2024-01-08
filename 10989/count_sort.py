count=[0 for _ in range(10_001)]
import sys
input=sys.stdin.readline
N=int(input())
for i in range(N):
    n=int(input())
    count[n]+=1
#for i in range(10_001):
#    if 0<count[i]: print('\n'.join([str(i) for _ in range(count[i])]))
for i in range(10_001):
    for _ in range(count[i]):
        print(i)

