# https://www.acmicpc.net/problem/4195
def union(x,y):
    if c[x]>c[y]:
        p[y]=x
        c[x]=c[x]+c[y]
    else:
        p[x]=y
        c[y]=c[x]+c[y]

def find_set(x):
    r=x
    while p[r]!=r:
        r=p[r]
    while p[x]!=x:
        y=p[x]
        p[x]=r
        x=y
    return x

import sys
input=sys.stdin.readline
T=int(input())
p=[i for i in range(200_001)]
c=[1 for i in range(200_001)]
for i in range(T):
    F=int(input())
    next_id=1
    dic={}
    for i in range(F):
        a,b=input().split()
        if a in dic:
            a_id=dic[a]
        else:
            dic[a]=next_id
            a_id=next_id
            p[a_id]=a_id
            c[a_id]=1
            next_id+=1
        if b in dic:
            b_id=dic[b]
        else:
            dic[b]=next_id
            b_id=next_id
            p[b_id]=b_id
            c[b_id]=1
            next_id+=1
        ra=find_set(a_id)
        rb=find_set(b_id)
        if ra==rb:
            print(c[ra])
        else:
            union(ra,rb)
            print(c[find_set(ra)])
