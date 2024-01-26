padovan_cache=[-1 for _ in range(101)]
padovan_cache[1],padovan_cache[2],padovan_cache[3],padovan_cache[4],padovan_cache[5]=1,1,1,2,2

def padovan(n):
    if 1<=n<=5: return padovan_cache[n]
    else:
        if -1==padovan_cache[n]: padovan_cache[n]=padovan(n-1)+padovan(n-5)
        return padovan_cache[n]

import sys
T=int(sys.stdin.readline())
for _ in range(T):
    print(padovan(int(sys.stdin.readline())))
    
