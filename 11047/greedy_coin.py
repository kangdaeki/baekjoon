# to speed up the slow input()
import sys
input = sys.stdin.readline
N,K=map(int,input().split())
coins=[]
for i in range(N):
    coins.append(int(input()))
ncoins=0
for i in range(N-1,-1,-1):
    c_i=coins[i]
    if c_i<=K:
        ncoins+=K//c_i
        K%=c_i
print(ncoins)
