N,M=map(int,input().split())
b=[i+1 for i in range(N)]
for _ in range(M):
    i,j=map(int,input().split())
    for k in range(i,i+(j-i)//2+1):
        b[k-1],b[j-k+i-1]=b[j-k+i-1],b[k-1]
print(*b)

