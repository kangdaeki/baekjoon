def gcd(x,y):
    if x<y: x,y=y,x
    while x>0 and y>0:
        x=x%y
        if x<y: x,y=y,x
    return x

a,b=map(int,input().split())
c,d=map(int,input().split())
e=a*d+b*c
f=b*d
g=gcd(e,f)
print(e//g,f//g)
