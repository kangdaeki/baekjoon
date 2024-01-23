import sys
N=int(sys.stdin.readline())
c=1
div=2
while div<N:
    if 1==N%2:
        if 0==N%div: 
            if 0<(N//div-div//2): c+=1
            else: break
        elif 0==(2*N)%div:
            if 0<(N//div-div//2+1): c+=1
            else: break
    else:
        if 0==N%div and 1==div%2: 
            if 0<(N//div-div//2): c+=1
            else: break
        elif 0==(2*N)%div and 0!=N%div:
            if 0<(N//div-div//2+1): c+=1
            else: break
    div+=1
print(c)


