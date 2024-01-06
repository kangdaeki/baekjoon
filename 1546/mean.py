N=int(input())
nums=list(map(int,input().split()))
max_num=max(nums)
my_sum=0
for n in nums:
    my_sum+=n*100/max_num
print(my_sum/N)
