def dot(N):
    if 1==N:
        return 3
    else:
        return (2*dot(N-1)-1)

N=int(input())
print(dot(N)**2)
