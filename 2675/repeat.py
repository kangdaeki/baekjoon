T=int(input())
for _ in range(T):
    R_str,S=input().split()
    R=int(R_str)
    for c in S:
        for j in range(R):
            print(c,end='')
    print()

