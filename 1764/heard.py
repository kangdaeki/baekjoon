N,M=map(int,input().split())
h=set()
for _ in range(N): h.add(input())
s=set()
for _ in range(M):
    ss=input()
    if ss in h: s.add(ss)
if 0==len(s): print(0)
else: print(len(s),*sorted(s),sep='\n')
