import sys
n=int(sys.stdin.readline())
g=[0 for _ in range(673_366)]
g[1],s,i=1,1,1
while s<n:
    i+=1
    g[i]=1+g[i-g[g[i-1]]]
    s+=g[i]
print(i)

