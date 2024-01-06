from typing import Dict
from typing import List

N=int(input())
tree:Dict[int,List]={}
for _ in range(N-1):
    l,r=map(int,input().split())
    if l not in tree: tree[l]=[r]
    else: tree[l].append(r)
    if r not in tree: tree[r]=[l]
    else: tree[r].append(l)
parent:List[int]=[-1 for _ in range(N+1)]
parent[0]=0
parent[1]=0
from collections import deque
q=deque()
q.append(1)
while q:
    i=q.popleft()
    for j in tree[i]:
        if -1==parent[j]: # not visited
            parent[j]=i
            q.append(j)
for i in range(2,N+1):
    print(parent[i])
