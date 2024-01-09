N=int(input())
if 0==N or 1==N: print(1)
else:
    f=1
    for i in range(2,N+1): f*=i
    print(f)
    
