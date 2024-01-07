ans=int(input())
n=int(input())
sum=0
for _ in range(n):
    price,nitems=map(int,input().split())
    sum+=(price*nitems)
if sum==ans: print("Yes")
else: print("No")
