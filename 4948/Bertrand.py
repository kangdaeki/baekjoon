c=[]
max_N=0
while True:
    n=int(input())
    if 0==n: break
    c.append(n)
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
    count=0
    for i in range(n+1,2*n+1):
        if sieve[i]: count+=1
    print(count)

