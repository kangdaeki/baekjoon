import sys
input=sys.stdin.readline
N,K=map(int,input().split())

def fact(N):
    f=1
    for i in range(1,N+1):
        f*=i
    return f

print(int(fact(N)/(fact(N-K)*fact(K))))
