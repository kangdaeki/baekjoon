A=[]
for i in range(9):
        A.append(list(map(int,input().split())))
max_n=A[0][0]
max_x,max_y=0,0
for i in range(9):
    for j in range(9):
        if  A[i][j]>max_n:
            max_n,max_x,max_y=A[i][j],j,i
print(max_n)
print(max_y+1,max_x+1)

