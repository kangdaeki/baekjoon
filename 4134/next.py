T=int(input())
c=[0 for _ in range(T)]
max_N=0
for i in range(T):
    n=int(input())
    c[i]=n
    if max_N<n: max_N=n
max_N=2*max_N
sieve=[True for _ in range(max_N+1)]
sieve[0],sieve[1]=False,False
for i in range(2,max_N+1):
    if sieve[i]:
        j=i+i
        while j<=max_N:
            sieve[j]=False
            j+=i
for n in c:
    for i in range(n,2*n+1):
        if sieve[i]: 
            print(i)
            break
