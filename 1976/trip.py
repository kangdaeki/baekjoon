# to speed up the slow input()
import sys
input = sys.stdin.readline

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

N=int(input())
# MAKE-SET
p=[i for i in range(N)]
M=int(input())
trip_map=[[0 for j in range(N)] for i in range(N)]
for i in range(N):
    trip_map[i]=list(map(int,input().split()))
for i in range(N):
    for j in range(N):
        if 1==trip_map[i][j]:
            union(i,j)
plan=[]
plan=list(map(int,input().split()))
if 1==len(plan): 
    print("YES")
    exit()
for i in range(len(plan)-1):
    if not is_same(plan[i]-1,plan[i+1]-1):
        print("NO")
        exit()
print("YES")

