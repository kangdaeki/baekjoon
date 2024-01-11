sl=[]
max_len=0
for _ in range(5):
    s=input()
    if max_len<len(s): max_len=len(s)
    sl.append(s)
for j in range(max_len):
    for i in range(5):
        if len(sl[i])>j:
            print(sl[i][j],end='')

