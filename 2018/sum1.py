import sys
N=int(sys.stdin.readline())
c,l,r,s=1,1,2,3
while r<N:
    if s==N: c,l,s=c+1,l+1,s-l
    elif s<N: r,s=r+1,s+r+1
    else: l,s=l+1,s-l
print(c)

