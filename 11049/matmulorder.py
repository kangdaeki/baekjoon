import sys
input=sys.stdin.readline
n=int(input())
rc=[]
for _ in range(n):
    rc.append(tuple(map(int,input().split())))
p=[rc[0][0]]
for i in range(0,n):
    p.append(rc[i][1])
m=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(0,n+1):
    m[i][i]=0
for r in range(1,n):
    for i in range(1,n-r+1):
        j=i+r
        m[i][j]=m[i][i]+m[i+1][j]+p[i-1]*p[i]*p[j]
        for k in range(i+1,j):
            mk=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
            if m[i][j]>mk:
                m[i][j]=mk
print(m[1][n])
