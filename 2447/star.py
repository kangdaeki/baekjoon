pattern= [ [1,1,1],[1,0,1],[1,1,1] ]
N=int(input())
backup=[]
result=[]
for _ in range(N):
    backup.append([0 for _ in range(N)])
    result.append([0 for _ in range(N)])
factor=3
for j in range(factor):
    for i in range(factor):
        result[i][j],backup[i][j]=pattern[i][j],pattern[i][j]
while N>factor:
    for j in range(factor):
        for i in range(factor):
            result[3*i][3*j],result[3*i][3*j+1],result[3*i][3*j+2]=backup[i][j],backup[i][j],backup[i][j]
            result[3*i+1][3*j],result[3*i+1][3*j+1],result[3*i+1][3*j+2]=backup[i][j],0,backup[i][j]
            result[3*i+2][3*j],result[3*i+2][3*j+1],result[3*i+2][3*j+2]=backup[i][j],backup[i][j],backup[i][j]
    for j in range(3*factor):
        for i in range(3*factor):
            backup[i][j]=result[i][j]
    factor*=3
for j in range(factor):
    for i in range(factor):
        if 1==result[i][j]: print('*',end='')
        else: print(' ',end='')
    print()
