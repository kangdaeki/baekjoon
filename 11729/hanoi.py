def hanoi(n,f,t,u):
    if 0>=n: return
    elif 1==n: print(f,t)
    else:
        hanoi(n-1,f,u,t)
        print(f,t)
        hanoi(n-1,u,t,f)

N=int(input())
print(2**N-1)
hanoi(N,1,3,2)

