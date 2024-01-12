N=int(input())
from collections import deque
dq=deque()
for i in range(1,N+1):
    dq.append(i)
while 1<len(dq):
    dq.popleft()
    dq.append(dq.popleft())
print(dq.popleft())
