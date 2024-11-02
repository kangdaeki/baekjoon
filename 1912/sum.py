import sys
input=sys.stdin.readline
N=int(input())
num=list(map(int,input().split()))
cost=[0 for j in range(N)]
max_sum,cost[0]=num[0],num[0]
for i in range(1,N):
    cost[i]=max(num[i],num[i]+cost[i-1])
    max_sum=max(cost[i],max_sum)
print(max_sum)

