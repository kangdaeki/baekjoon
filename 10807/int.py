N=int(input())
v_list=list(map(int,input().split()))
v=int(input())
c=0
for n in v_list: 
    if n==v: c+=1
print(c)
