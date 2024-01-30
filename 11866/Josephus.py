N,K=map(int,input().split())
l=[i+1 for i in range(N)]
i=0
r=[]
for _ in range(N):
    c=1
    while c<K:
        if -1==l[i]:
            i+=1
            if N<=i: i=0
        else:
            c+=1
            i+=1
            if N<=i: i=0
    while -1==l[i]:
        i+=1
        if N<=i: i=0
    r.append(l[i])
    l[i]=-1
print('<',end='')
print(r[0],end='')
for i in range(1,N):  print(',',r[i],end='')
print('>')
