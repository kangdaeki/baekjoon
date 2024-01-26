memo=[[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
visited=[[[False for _ in range(21)] for _ in range(21)] for _ in range(21)]
def w(a,b,c):
    if 0>=a or 0>=b or 0>=c: return 1
    if 20<a or 20<b or 20<c: 
        if visited[20][20][20]: return memo[20][20][20] 
        else:
            memo[20][20][20]=w(20,20,20)
            visited[20][20][20]=True
            return memo[20][20][20]
    if visited[a][b][c]: return memo[a][b][c]
    if a<b and b<c: 
        if not visited[a][b][c-1]:
            memo[a][b][c-1]=w(a,b,c-1)
            visited[a][b][c-1]=True
        if not visited[a][b-1][c-1]:
            memo[a][b-1][c-1]=w(a,b-1,c-1)
            visited[a][b-1][c-1]=True
        if not visited[a][b-1][c]:
            memo[a][b-1][c]=w(a,b-1,c)
            visited[a][b-1][c]=True
        return memo[a][b][c-1]+memo[a][b-1][c-1]-memo[a][b-1][c]
    if not visited[a-1][b][c]:
        memo[a-1][b][c]=w(a-1,b,c)
        visited[a-1][b][c]=True
    if not visited[a-1][b-1][c]:
       memo[a-1][b-1][c]=w(a-1,b-1,c)
       visited[a-1][b-1][c]=True
    if not visited[a-1][b][c-1]:
        memo[a-1][b][c-1]=w(a-1,b,c-1)
        visited[a-1][b][c-1]=True
    if not visited[a-1][b-1][c-1]:
        memo[a-1][b-1][c-1]=w(a-1,b-1,c-1)
        visited[a-1][b-1][c-1]=True
    return memo[a-1][b][c]+memo[a-1][b-1][c]+memo[a-1][b][c-1]-memo[a-1][b-1][c-1]

while True:
    a,b,c=map(int,input().split())
    if -1==a and -1==b and -1==c: exit()
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
    
