# to speed up the slow input()
#import sys
#input = sys.stdin.readline
while True:
    X,Y=map(int,input().split())
    if 0==X and 0==Y: break
    A,B=max(X,Y),min(X,Y)
    while A>0 and B>0:
        A=A%B
        if A<B: A,B=B,A
    if 1==A: print('neither')
    elif X>Y: print('multiple')
    else: print('factor')
