N,M=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
len_l=len(l)
my_sum=0
for i in range(len_l):
    if l[i]>M: break
    for j in range(i+1,len_l):
        if l[i]+l[j]>M: break
        for k in range(j+1,len_l):
            if l[i]+l[j]+l[k]>M: break
            if my_sum<l[i]+l[j]+l[k]: my_sum=l[i]+l[j]+l[k]
print(my_sum)
