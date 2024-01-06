import sys
input=sys.stdin.readline
V,E=map(int,input().split())
K=int(input())
graph=collections.defaultdict(list)
E_set={}
for _ in range(E):
    u,v,w=map(int,input().split())
    if (u,v) in E_set:
    else:
        graph[u].append((v,w))
    if (u,v) in E_set:
        if w<E_set[(u,v)]: 
            E_set[(u,v)]=w
    elif (v,u) in E_set:
        if w<E_set[(v,u)]: 
            E_set[(v,u)]=w
    else: 
        E_set[(u,v)]=w
Q={(0,K)}

