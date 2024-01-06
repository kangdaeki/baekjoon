from typing import List
import copy
def matmul_remainder(M:List,N:List,R:int)->List:
    V=copy.deepcopy(M)
    n=len(M)
    for i in range(n):
        for j in range(n):
            V[i][j]=0
            for k in range(n):
                V[i][j]=(V[i][j]+M[i][k]*N[k][j])%R
    return V

def matpow_remainder(M:List, n:int, R:int)->List:
    S=copy.deepcopy(M)
    X=copy.deepcopy(M)
    for i in range(len(S)):
        for j in range(len(S[i])):
            if i==j:
                S[i][j]=1
            else:
                S[i][j]=0
    while n>0:
        if n%2:
            S=matmul_remainder(S,X,R)
        n=n//2
        X=matmul_remainder(X,X,R)
    return S

# to speed up the slow input()
import sys
input = sys.stdin.readline
N=int(input())
M=[[1,1],[1,0]]
print(matpow_remainder(M, N, 10007)[0][0])
