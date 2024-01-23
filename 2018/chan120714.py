n=int(input())-1
res=1
a=1
while n>0:
    a+=1
    n-=a
    if n%a==0:
        res+=1
print(res)
