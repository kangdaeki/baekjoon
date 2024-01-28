import sys
input=sys.stdin.readline
T=int(input())
cases=[0 for _ in range(T)]
max_N=0
for i in range(T):
    cases[i]=int(input())
    if cases[i]>max_N: max_N=cases[i]
sieve=[True for _ in range(max_N+1)]
sieve[0],sieve[1]=False,False
for i in range(2,max_N+1):
    if sieve[i]:
        j=i+i
        while j<=max_N:
            sieve[j]=False
            j+=i
for i in range(T):
    count=0
    mid=cases[i]//2
    for j in range(2,mid+1):
        if sieve[j] and sieve[cases[i]-j]: count+=1
    print(count)
