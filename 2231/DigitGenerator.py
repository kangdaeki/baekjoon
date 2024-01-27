N=int(input())
for i in range(N+1):
    i_str=str(i)
    my_sum=i
    for j in i_str: my_sum+=int(j)
    if my_sum==N: 
        print(i)
        exit()
print(0)
