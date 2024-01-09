N=int(input())
for i in range(N-1,-1,-1):
    for j in range(i):
        print(' ',end='')
    for j in range(0,2*(N-i)-1):
        print('*',end='')
    print()
for i in range(1,N):
    for j in range(i):
        print(' ',end='')
    for j in range(2*(N-i)-1,0,-1):
        print('*',end='')
    print()
