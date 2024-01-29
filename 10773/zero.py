import sys
input=sys.stdin.readline
K=int(input())
s=[]
for _ in range(K):
    n=int(input())
    if 0!=n: s.append(n)
    else: s.pop()
print(sum(s))

