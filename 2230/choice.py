import sys
input=sys.stdin.readline
N,M=map(int,input().split())
nums=[]
for _ in range(N): nums.append(int(input()))
nums.sort()
min_diff,l,r=sys.maxsize,0,1
while r<N and l<=r:
    diff=nums[r]-nums[l]
    if diff>=M:
        if min_diff>diff:  min_diff=diff
        l=l+1
    else: r=r+1 
print(min_diff)

