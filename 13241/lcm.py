X,Y=map(int,input().split())
A,B=X,Y
if A<B: A,B=B,A
while A>0 and B>0:
    A=A%B
    if A<B: A,B=B,A
print(int(X/A*Y))
