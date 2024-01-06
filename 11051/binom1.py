import sys
input=sys.stdin.readline
N,K=map(int,input().split())
R=10_007
n_c_k=[[0 for _ in range(K+1)] for _ in range(N+1)]
for n in range(N+1):
    n_c_k[n][0]=1
for k in range(K+1):
    if k<=n:
        n_c_k[k][k]=1

for n in range(2,N+1):
    for k in range(1,K+1):
        if k>n: break
        n_c_k[n][k]=(n_c_k[n-1][k]+n_c_k[n-1][k-1])%R
print(n_c_k[N][K])
