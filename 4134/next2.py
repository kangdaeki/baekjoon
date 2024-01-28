def is_prime(n):
    if 0==n or 1==n: return False
    if 2==n: return True
    if 0==n%2: return False
    i=3
    while i*i<=n:
        if 0==n%i: return False
        i+=2
    return True

T=int(input())
for i in range(T):
    n=int(input())
    while not is_prime(n):
        n+=1
    print(n)
