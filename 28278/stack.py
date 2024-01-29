import sys
input=sys.stdin.readline
N=int(input())
st=[]
for _ in range(N):
    s=input()
    if '1'!=s[0]: o=int(s)
    else: o,x=map(int,s.split())
    if 1==o:
        st.append(x)
    elif 2==o:
        if 0>=len(st): print(-1)
        else: print(st.pop())
    elif 3==o:
        print(len(st))
    elif 4==o:
        if 0>=len(st): print(1)
        else: print(0)
    elif 5==o:
        if 0>=len(st): print(-1)
        else: print(st[len(st)-1])


