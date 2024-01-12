def dfs(u):
    visited[u]=True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

V=int(input())
graph=[[] for _ in range(V+1)]
E=int(input())
for _ in range(E):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited=[False for _ in range(V+1)]
dfs(1)
count=0
for i in range(V+1):
    if visited[i]: count+=1
print(count-1) # except 1
