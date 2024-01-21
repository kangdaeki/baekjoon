def has666(n):
    count=0
    while n>0:
        if 6==n%10: count+=1
        else: count=0
        if 3==count: return True
        n=n//10
    return False

N=int(input())
index=1
number=665
while True:
    while not has666(number): number+=1
    if N>index:
        index+=1
        number+=1
    else: break
print(number)

