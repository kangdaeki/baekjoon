# to speed up the slow input()
import sys
input = sys.stdin.readline
N,K=map(int,input().split())
K-=1 # list index starts from 0
A=list(map(int,input().split()))
A.sort()
print(A[K])

