import sys
input=sys.stdin.readline
N,M=map(int,input().split())
nums=list(map(int,input().split()))
prefix_sum=[0 for _ in range(N+1)]
for i in range(N):
    prefix_sum[i+1]=prefix_sum[i]+nums[i]
for _ in range(M):
    i,j=map(int,input().split())
    print(prefix_sum[j]-prefix_sum[i-1])
