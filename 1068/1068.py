from typing import List
def kill_children(parent:List, kill:int):
    parent[kill]=-2
    for i in range(len(parent)):
        if (kill==parent[i]): kill_children(parent,i)

def kill_nonleaf(parent:List):
    result=parent[:]
    for i in range(len(parent)):
        if (-2!=parent[i] and -1!=parent[i]):
            result[parent[i]]=-2
    for i in range(len(parent)):
        parent[i]=result[i]

def count_rest(parent:List) -> int:
    count=0
    for i in range(len(parent)):
        if (-2!=parent[i]): count+=1
    return count

N=int(input())
parent=[*map(int,input().split())]
kill=int(input())
print(parent)
kill_children(parent, kill)
print(parent)
kill_nonleaf(parent)
print(parent)
print(count_rest(parent))
