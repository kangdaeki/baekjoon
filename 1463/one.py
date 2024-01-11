import sys
input=sys.stdin.readline
N=int(input())
c=[0 for _ in range(max(N+1,4))]
c[2],c[3]=1,1
for i in range(4,N+1):
    c[i]=c[i-1]+1 # 3
    if 0==i%2 and c[i//2]+1<c[i]: c[i]=c[i//2]+1
    if 0==i%3 and c[i//3]+1<c[i]: c[i]=c[i//3]+1
print(c[N])

