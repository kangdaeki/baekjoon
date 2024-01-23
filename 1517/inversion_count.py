def merge_sort(s,e):
    global count
    if e<=s: return
    m=s+(e-s)//2
    merge_sort(s,m)
    merge_sort(m+1,e)
    for i in range(s,e+1): merged[i]=A[i]
    mi,i1,i2=s,s,m+1
    while i1<=m and i2<=e:
        if merged[i1]>merged[i2]:
            A[mi]=merged[i2]
            count+=(i2-mi)
            mi,i2=mi+1,i2+1
        else:
            A[mi]=merged[i1]
            mi,i1=mi+1,i1+1
    while i1<=m:
            A[mi]=merged[i1]
            mi,i1=mi+1,i1+1
    while i2<=e:
            A[mi]=merged[i2]
            mi,i2=mi+1,i2+1

count=0
import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
merged=[0 for _ in range(N)]
merge_sort(0,N-1)
print(count)

