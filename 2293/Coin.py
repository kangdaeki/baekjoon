n,k=map(int,input().split())
coins=[0 for i in range(n)]
for i in range(n):
    coins[i]=int(input())
coins=sorted(coins)
counts=[0 for i in range(10_001)]
counts[0]=1
for i in range(n):
    if coins[i]>k:
        break
    counts[coins[i]]+=1
    for j in range(coins[i]+1,k+1):
        counts[j]+=counts[j-coins[i]]
print(counts[k])
