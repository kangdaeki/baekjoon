import sys
input=sys.stdin.readline
N,M=map(int,input().split())
nums=list(map(int,input().split()))
if 1==N: 
    if nums[0]==M: print(1)
    else: print(0)
else:
    p1,p2,s,c=0,1,nums[0]+nums[1],0
    if nums[0]==M: c=1
    while p1<N and p2<N:
        if s==M: c,s,p1=c+1,s-nums[p1],p1+1
        elif s>M:
            s,p1=s-nums[p1],p1+1
        else:
            p2=p2+1
            if p2<N: s=s+nums[p2]
    print(c)
