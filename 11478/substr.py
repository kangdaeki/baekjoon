S=input()
s=set()
for i in range(0,len(S)):
    for j in range(i,len(S)):
        s.add(S[i:j+1])
print(len(s))
