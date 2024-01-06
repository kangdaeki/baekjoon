N=int(input())
data=list(map(int,input().split()))
data.sort()
M=int(input())
search=list(map(int,input().split()))
from bisect import bisect_left
for n in search:
    index=bisect_left(data,n)
    if N==index or n!=data[index]: print(0)
    else: print(1)
