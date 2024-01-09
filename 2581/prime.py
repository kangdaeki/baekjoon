M=int(input())
N=int(input())
sieve=[True for _ in range(N+1)]
if 1<=N: 
    sieve[0],sieve[1]=False,False
import math
for i in range(2,1+int(math.sqrt(N))):
    j=2
    while i*j<=N:
        sieve[i*j]=False
        j=j+1
sum_n=0
min_n=N+1
for i in range(M,N+1):
    if sieve[i]: 
        sum_n+=i
        if i<min_n: min_n=i
if 0==sum_n:
    print(-1)
else:
    print(sum_n)
    print(min_n)
