s=set()
n=int(input())
for _ in range(n):
    name,action=input().split()
    if 'enter'==action: s.add(name)
    elif 'leave'==action: s.remove(name)
print(*sorted(s,reverse=True),sep='\n')

