import sys
input=sys.stdin.readline

n_colors=int(input())
colors=list(map(int,input().split()))
n_pebbles=sum(colors)
pick=int(input())

prob=0.0
for i in range(n_colors):
    fact=1.0
    if pick<=colors[i]:
        for j in range(pick):
            fact*=((colors[i]-j)/(n_pebbles-j))
        prob+=fact
print(prob)
