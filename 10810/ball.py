N,M=map(int,input().split())
ball_bin=[0 for _ in range(N)]
for _ in range(M):
    s,e,n=map(int,input().split())
    for i in range(s-1,e): ball_bin[i]=n
print(*ball_bin)
