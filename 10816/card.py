import sys
input=sys.stdin.readline
N=int(input())
d={}
nl=list(map(int,input().split()))
for x in nl:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
M=int(input())
ml=list(map(int,input().split()))
for x in ml:
    if x in d:
        print(d[x],end=' ')
    else:
        print(0,end=' ')

