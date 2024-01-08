A,B=map(int,input().split())
d=A//B
print(d,end='')
r=A%B
if 0!=r:
    print('.',end='')
    i=0
    while 0!=r and i<=1000:
        r*=10
        i+=1
        print(r//B,end='')
        r%=B
print()
