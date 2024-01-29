def find_gcd(x,y): 
    while y: x,y=y,x%y 
    return x 

def find_gcd_multiple(l):
    if 1==len(l): return l[0]
    elif 2==len(l): return find_gcd(l[0],l[1])
    n1=l[0] 
    n2=l[1] 
    gcd=find_gcd(n1,n2) 
    for i in range(2,len(l)): gcd=find_gcd(gcd,l[i]) 
    return gcd

N=int(input())
l=[]
for _ in range(N): l.append(int(input()))
m=[]
for i in range(N-1): m.append(l[i+1]-l[i])

gcd=find_gcd_multiple(m)

count=0
for i in range(1,N): 
    count+=(l[i]-l[i-1])//gcd-1
print(count)
