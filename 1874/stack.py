n=int(input())
from collections import deque
iq=deque() # input queue
rq=deque() # result queue
for i in range(n): 
    iq.append(i+1)
    rq.append(int(input()))
st=[] # stack
p=[]
while rq:
    if not st or (iq and iq[0]<=rq[0]):
        r=rq.popleft()
        while iq and iq[0]<=r:
            i=iq.popleft()
            st.append(i)
            p.append("+")
        st.pop()
        p.append("-")
    else:
        if rq[0]==st[-1]:
            rq.popleft()
            st.pop()
            p.append("-")
        else:
            print("NO")
            exit()
print(*p,sep='\n')


