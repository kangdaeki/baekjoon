T=int(input())
for _ in range(T):
    s=input()
    st=[]
    empty_pop=False
    for c in s:
        if '('==c:
            st.append('(')
        elif ')'==c:
            if 0<len(st): st.pop()
            else:
                empty_pop=True
                break
    if empty_pop: print('NO')
    elif 0==len(st): print('YES')
    else: print('NO')
