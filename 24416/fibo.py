def fibonacci(n):
    global count_fibonacci
    f=[0 for _ in range(n+1)]
    f[1]=1
    f[2]=1
    for i in range(3,n+1): 
        count_fibonacci+=1
        f[i]=f[i-1]+f[i-2]
    return f[n]

n=int(input())
count_fibonacci=0
print(fibonacci(n),count_fibonacci)

