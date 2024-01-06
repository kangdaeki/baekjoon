# to speed up the slow input()
#import sys
#input = sys.stdin.readline
s1=input()
s2=input()
m,n=len(s1),len(s2)
table=[[0 for j in range(n+1)] for i in range(m+1)]
back=[[0 for j in range(n+1)] for i in range(m+1)]
# 0: match, 1: right, -1: down
for i in range(1,m+1): back[i][0]=-1
for j in range(1,n+1): back[0][j]=1
for i in range(1,m+1):
    for j in range(1,n+1):
        if s1[i-1]==s2[j-1]:
            table[i][j]=table[i-1][j-1]+1
            back[i][j]=0
        else:
            table[i][j]=max(table[i-1][j],table[i][j-1])
            if table[i-1][j]>table[i][j-1]:
                back[i][j]=-1
            else:
                back[i][j]=1
print(table[m][n])
if table[m][n]>0:
    lcs=[]
    i,j=m,n
    while i>=0 and j>=0:
        if i==0 and j==0: break
        if back[i][j]==0:
            lcs.append(s1[i-1])
            i,j=i-1,j-1
        elif back[i][j]==1:
            j-=1
        else: # back[i][j]==-1:
            i-=1
    lcs=''.join(lcs)
    print(lcs[::-1])
