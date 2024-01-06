import sys
input=sys.stdin.readline
N,M=map(int,input().split())
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))
B=[]
M,K=map(int,input().split())
for i in range(M):
    B.append(list(map(int,input().split())))
C=[]
for i in range(N):
    C.append([])
    for j in range(K):
        sum=0
        for k in range(M):
            sum+=A[i][k]*B[k][j]
        C[i].append(sum)
for i in range(N):
    print(*C[i],sep=' ')
