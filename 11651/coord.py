def my_cmp(p1,p2):
    if p1[1]>p2[1]: return 1
    elif p1[1]<p2[1]: return -1
    elif p1[0]>p2[0]: return 1
    elif p1[0]<p2[0]: return -1
    else: return 0

N=int(input())
l=[]
for _ in range(N): l.append(tuple(map(int,input().split())))
from functools import cmp_to_key
l.sort(key=cmp_to_key(my_cmp))
for x,y in l: print(x,y)
