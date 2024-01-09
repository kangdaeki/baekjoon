N=int(input())
M=1_000
sieve=[True for _ in range(M+1)]
sieve[0],sieve[1]=False,False
import math
for i in range(2,1+int(math.sqrt(M))):
    j=2
    while i*j<=M:
        sieve[i*j]=False
        j=j+1
num=map(int,input().split())
count=0
for i in num:
    if sieve[i]: count+=1
print(count)
