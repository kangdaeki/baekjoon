# to speed up the slow input()
#import sys
#input = sys.stdin.readline
s1=input()
s2=input()
m,n=len(s1),len(s2)
table=[[0 for j in range(n+1)] for i in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if s1[i-1]==s2[j-1]:
            table[i][j]=table[i-1][j-1]+1
        else:
            table[i][j]=max(table[i-1][j],table[i][j-1])
print(table[m][n])
ans=input()
print(len(ans))
if len(ans)==table[m][n]:
    print("YES")
else: print("NO")
