# to speed up the slow input()
import sys
input = sys.stdin.readline
A,B=map(int,input().split())
if A<B: A,B=B,A
while A>0 and B>0:
    A=A%B
    if A<B: A,B=B,A
for _ in range(A):
    print("1",end="")
