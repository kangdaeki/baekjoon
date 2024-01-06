def merge_sort(l,r):
    if l>=r: return
    mid=l+(r-l)//2
    merge_sort(l,mid)
    merge_sort(mid+1,r)
    p=l
    q=mid+1
    t=l
    while p<=mid and q<=r:
        if data[p]<data[q]:
            buffer[t]=data[p]
            p+=1
        else: # data[p]>data[q] since all valuaes are distinct
            buffer[t]=data[q]
            q+=1
        t+=1
    while p<=mid:
        buffer[t]=data[p]
        p+=1
        t+=1
    while q<=r:
        buffer[t]=data[q]
        q+=1
        t+=1
    for i in range(l,r+1):
        data[i]=buffer[i]

# to speed up the slow input()
import sys
input = sys.stdin.readline
N=int(input())
data=[0 for _ in range(N)]
buffer=[0 for _ in range(N)]
for i in range(N):
    data[i]=int(input())
#print(data)
merge_sort(0,N-1)
for i in range(N):
    print(data[i])

