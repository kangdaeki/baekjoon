import sys
input=sys.stdin.readline
N,M=map(int,input().split())
pokemon_list=[]
pokemon_dict={}
for i in range(N):
    name=input().rstrip()
    pokemon_list.append(name)
    pokemon_dict[name]=i+1
for _ in range(M):
    s=input().rstrip()
    if s.isnumeric(): print(pokemon_list[int(s)-1])
    else: print(pokemon_dict[s])

