N,M=map(int,input().split())
m=[]
for _ in range(N):
    m.append(list(input()))
from collections import deque
y,x=0,0
m[y][x]='0'
count=1
dq=deque([(y,x,count)])
while dq:
    y,x,count=dq.popleft()
    if N-1==y and M-1==x: break;
    if 0<y and '1'==m[y-1][x]: 
        m[y-1][x]='0'
        dq.append((y-1,x,count+1))
    if N-1>y and '1'==m[y+1][x]: 
        m[y+1][x]='0'
        dq.append((y+1,x,count+1))
    if 0<x and '1'==m[y][x-1]: 
        m[y][x-1]='0'
        dq.append((y,x-1,count+1))
    if M-1>x and '1'==m[y][x+1]: 
        m[y][x+1]='0'
        dq.append((y,x+1,count+1))
print(count)
