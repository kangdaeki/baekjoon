N=int(input())
f=[0,1]
if 0==N: print(0)
elif 1==N: print(1)
else:
    for i in range(2,N+1):
        f.append(f[i-1]+f[i-2])
    print(f[N])
    
