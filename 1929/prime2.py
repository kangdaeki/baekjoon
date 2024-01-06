import sys
input=sys.stdin.readline
M,N=map(int,input().split())
sieve=[True for _ in range(N+1)]
sieve[0]=False
sieve[1]=False
import math
sqrt_n=int(math.sqrt(N))
for i in range(2,sqrt_n+2):
    j=2
    factor=i*j
    while factor<=N:
        sieve[factor]=False
        j+=1
        factor+=i
for i in range(M,N+1):
    if sieve[i]: print(i)
