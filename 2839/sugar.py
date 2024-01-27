N=int(input())
m=[-1 for _ in range(N+1)]
m[0]=0
m[3]=1
if 5<=N: m[5]=1
for i in range(6,N+1):
    if -1!=m[i-3] and -1!=m[i-5]: m[i]=1+min(m[i-3],m[i-5])
    elif -1!=m[i-3] and -1==m[i-5]: m[i]=1+m[i-3]
    elif -1==m[i-3] and -1!=m[i-5]: m[i]=1+m[i-5]
    else: m[i]=-1
print(m[N])

