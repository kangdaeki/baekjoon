min_v=1_000_001
max_v=-1_000_001
N=int(input())
nums=map(int,input().split())
for n in nums:
    if n<min_v: min_v=n
    if n>max_v: max_v=n
print(min_v,max_v)
