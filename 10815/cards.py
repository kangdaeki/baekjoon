import sys
input=sys.stdin.readline
N=int(input())
my_nums=list(map(int,input().split()))
plus_map=[0 for _ in range(10_000_001)]
minus_map=[0 for _ in range(10_000_001)]
for n in my_nums:
    if n>=0: plus_map[n]=1
    else: minus_map[-n]=1
M=int(input())
your_nums=list(map(int,input().split()))
for n in your_nums:
    if n>=0: print(plus_map[n], end=' ')
    else: print(minus_map[-n], end=' ')
print()
