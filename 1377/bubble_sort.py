import sys
input=sys.stdin.readline
N=int(input())
A=[]
for i in range(N): A.append((int(input()),i))
A=sorted(A)
print(1+max([a[1]-j for j,a in enumerate(A)]))
