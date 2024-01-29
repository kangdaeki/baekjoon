import sys
input=sys.stdin.readline
N=int(input())
l=list(map(int,input().split()))
st,li,oi=[],0,1
while oi<=N:
    if li<N and oi==l[li]: li,oi=li+1,oi+1
    elif st and oi==st[len(st)-1]: 
        oi+=1
        st.pop()
    elif li<N: 
        st.append(l[li])
        li+=1
    else: break
if li>=N and not st: print("Nice")
else: print("Sad")
