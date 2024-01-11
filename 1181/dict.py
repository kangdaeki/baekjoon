from functools import cmp_to_key

def compare(x,y):
    if len(x)>len(y):
        return 1
    elif len(x)<len(y):
        return -1
    else:
        if x<=y:
            return -1
        else:
            return 1
        return -1

T=int(input())
s=set()
for _ in range(T):
    s.add(input())
l=sorted(s,key=cmp_to_key(compare))
print(*l,sep='\n')
