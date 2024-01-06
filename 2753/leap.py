y=int(input())
if 0==y%4:
    if 0==y%100:
        if 0==y%400: print(1)
        else: print(0)
    else: print(1)
else: print(0)
