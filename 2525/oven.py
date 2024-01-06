h,m=map(int,input().split())
d=int(input())
h=(h+(m+d)//60)%24
m=(m+d)%60
print(h,m)
