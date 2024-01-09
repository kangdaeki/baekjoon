N,M=map(int,input().split())
b=[i+1 for i in range(N)]
for _ in range(M):
    i,j=map(int,input().split())
    b[i-1],b[j-1]=b[j-1],b[i-1]
print(*b)

