N,B=map(int,input().split())
t=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
r=[]
while N>=B:
    r.append(t[N%B])
    N=N//B
r.append(t[N%B])
print(''.join(r)[::-1])
