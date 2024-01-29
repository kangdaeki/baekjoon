import sys
for line in sys.stdin:
    if '.'==line[0]: break
    st=[]
    not_good=False
    for c in line:
        if '.'==c: break
        elif '('==c: st.append(c)
        elif '['==c: st.append(c)
        elif ')'==c: 
            if 0==len(st):
                not_good=True
                break
            if '('!=st.pop():
                not_good=True
                break
        elif ']'==c: 
            if 0==len(st):
                not_good=True
                break
            if '['!=st.pop():
                not_good=True
                break
    if not_good: print('no')
    elif 0!=len(st): print('no')
    else: print('yes')
