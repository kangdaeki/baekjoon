N=int(input())
x=[]
y=[]
for _ in range(N):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
a=min(x)
b=min(y)
c=max(x)
d=max(y)
print((c-a)*(d-b))
