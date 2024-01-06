import sys
input=sys.stdin.readline
N,K=map(int,input().split())
N_list=[i for i in range(N)]
from itertools import combinations
print(len(list(combinations(N_list,K))))
