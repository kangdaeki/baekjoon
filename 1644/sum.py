import sys
N=int(sys.stdin.readline())
if 1==N:
    print(0)
    exit()
if 2==N:
    print(1)
    exit()
sieve=[True for _ in range(N+1)]
sieve[0],sieve[1]=False,False
import math
for i in range(2,1+int(math.sqrt(N))):
    j=2
    while i*j<=N:
        sieve[i*j]=False
        j=j+1
nums=[]
for i in range(N+1):
    if sieve[i]: nums.append(i)
c,l,r,s=0,0,1,nums[0]+nums[1]
while r<len(nums):
    if s==N: c,l,s=c+1,l+1,s-nums[l]
    elif s<N: 
        r=r+1
        if r<len(nums): s=s+nums[r]
    else: l,s=l+1,s-nums[l]
print(c)

