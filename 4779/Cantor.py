def cantor(n):
    if 0==n: print("-",end='')
    elif 1==n: print("- -",end='')
    else:
        cantor(n-1)
        print(' '*(3**(n-1)),end='')
        cantor(n-1)

import sys
input=sys.stdin.readline
for line in sys.stdin:
    line=line.rstrip()
    if 0==len(line): exit()
    N=int(line)
    cantor(N)
    print()
