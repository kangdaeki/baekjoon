def compare(e1, e2):
    if e1[0]<e2[0]:
    	return -1
    elif e1[0]>e2[0]:
    	return 1
    else:
        if e1[1]<e2[1]:
            return -1
        elif e1[1]>e2[1]:
            return 1
        else:
            return 0

N=int(input())
l=[]
for _ in range(N):
    x,y=map(int,input().split())
    l.append((x,y))
from functools import cmp_to_key
l=sorted(l, key=cmp_to_key(compare))
for x,y in l:
    print(x,y)

