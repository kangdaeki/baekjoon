N=int(input())
[print(''.join([" " for j in range(N-1,i-1,-1)]),''.join(["*" for j in range(i)]),sep='') for i in range(1,N+1)]

