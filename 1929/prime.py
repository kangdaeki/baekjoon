M,N=map(int,input().split())
sieve=[True for _ in range(N+1)]
sieve[0],sieve[1]=False,False
import math
for i in range(2,1+int(math.sqrt(N))):
    j=2
    while i*j<=N:
        sieve[i*j]=False
        j=j+1
for i in range(M,N+1):
    if sieve[i]: print(i)
