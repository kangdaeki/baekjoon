def dfs(y,x,index):
    graph[y][x]=index
    if 0<y and -1==graph[y-1][x]: dfs(y-1,x,index)
    if 0<x and -1==graph[y][x-1]: dfs(y,x-1,index)
    if N-1>y and -1==graph[y+1][x]: dfs(y+1,x,index)
    if N-1>x and -1==graph[y][x+1]: dfs(y,x+1,index)

N=int(input())
graph=[]
for _ in range(N):
    l=input()
    ve=[]
    for val in l: ve.append(-int(val))
    graph.append(ve)
index=0
for y in range(N):
    for x in range(N):
        if -1==graph[y][x]:
            index+=1
            dfs(y,x,index)
print(index)
nums=[0 for _ in range(index)]
for y in range(N):
    for x in range(N):
        if 0!=graph[y][x]: nums[graph[y][x]-1]+=1
print(*sorted(nums),sep='\n')

