N,B_str=input().split()
B=int(B_str)
R=0
for c in N:
    if c.isnumeric(): R=R*B+int(c)
    elif c.isalpha(): R=R*B+(ord(c)-ord('A')+10)
print(R)
