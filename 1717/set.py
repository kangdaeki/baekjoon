# to speed up the slow input()
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
# MAKE-SET
p=[i for i in range(n+1)]

def union(x:int, y:int):
    x=find_set(x)
    y=find_set(y)
    if x!=y: p[y]=x

def is_same(x:int, y:int):
    x=find_set(x)
    y=find_set(y)
    if x!=y: return False
    else: return True

def find_set(x:int)->int:
    if x==p[x]: return x
    else: 
        p[x]=find_set(p[x])
        return p[x]

for _ in range(m):
    o,a,b=map(int,input().split())
    if 0==o: union(a,b)
    elif 1==o: 
        if is_same(a,b): print("YES")
        else: print("NO")

