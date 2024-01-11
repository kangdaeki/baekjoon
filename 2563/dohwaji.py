def inside(xl,yl,p):
    for x,y in p:
        if x<=xl<x+10 and y<=yl<y+10:
#            print(xl,yl)
            return True
    return False

T=int(input())
p=[]
for i in range(T):
    p.append(tuple(map(int,input().split())))
xs,ys=set(),set()
for x,y in p:
    xs.add(x)
    xs.add(x+10)
    ys.add(y)
    ys.add(y+10)
xl=sorted(xs)
yl=sorted(ys)
area=0
for i in range(len(yl)-1):
    for j in range(len(xl)-1):
        if inside(xl[j],yl[i],p):
#            print("Mul:",xl[j],yl[i],xl[j+1],yl[i+1])
            area+=(xl[j+1]-xl[j])*(yl[i+1]-yl[i])
print(area)
