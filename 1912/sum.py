import sys
input=sys.stdin.readline
N=int(input())
if 1==N: exit()
import math
for i in range(2,1+int(math.sqrt(N))):
    while 0==N%i:
       print(i)
       N=N//i
if 1!=N:
    print(N)
