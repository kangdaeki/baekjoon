def my_cmp(x1,x2):
    if x1[0]>x2[0]: return 1
    elif x1[0]<x2[0]: return -1
    else: return 0

N=int(input())
l=[]
for i,x in enumerate(map(int,input().split())): l.append((x,i))
from functools import cmp_to_key
sl=sorted(l,key=cmp_to_key(my_cmp))
r=[-1 for _ in range(len(l))]
k=0
ox=0
for j in range(len(sl)):
    x,i=sl[j]
    if 0==j:
        r[i]=k
        ox=x
    elif x!=ox:
        k+=1
        r[i]=k
        ox=x
    else: 
        r[i]=k
print(*r)
