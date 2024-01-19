def my_compare(x,y):
    if x[0]<y[0]: return -1
    elif x[0]>y[0]: return 1
    else: 
        if x[1]<y[1]: return -1
        else: return 1
    return 1

N=int(input())
l=[]
for i in range(N):
    age,name=input().split()
    age=int(age)
    l.append((age,i,name))
from functools import cmp_to_key
l=sorted(l,key=cmp_to_key(my_compare))
for age,i,name in l:
    print(age,name)
