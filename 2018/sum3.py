import sys
input=sys.stdin.readline # C 언어에서 gets
N=int(input())
count=1
p1=1
p2=2
my_sum=p1+p2
while p2<N and p1<N:
    if my_sum==N: 
        count=count+1
        p2=p2+1
        my_sum=my_sum+p2
    elif my_sum<N:
        p2=p2+1
        my_sum=my_sum+p2
    else: # my_sum>N
        my_sum=my_sum-p1
        p1=p1+1
print(count)
    
