def check_bw(j,i):
    ref=[ 'BWBWBWBW',
          'WBWBWBWB',
          'BWBWBWBW',
          'WBWBWBWB',
          'BWBWBWBW',
          'WBWBWBWB',
          'BWBWBWBW',
          'WBWBWBWB' ]
    count=0
    for y in range(8):
        for x in range(8):
            if ref[y][x]!=chess[i+y][j+x]: count+=1
    return count

def check_wb(j,i):
    ref=[ 'WBWBWBWB',
          'BWBWBWBW',
          'WBWBWBWB',
          'BWBWBWBW',
          'WBWBWBWB',
          'BWBWBWBW',
          'WBWBWBWB',
          'BWBWBWBW' ]
    count=0
    for y in range(8):
        for x in range(8):
            if ref[y][x]!=chess[i+y][j+x]: count+=1
    return count

N,M=map(int,input().split())
chess=[]
for _ in range(N):
    chess.append(input())
min_color=64
for i in range(N-8+1):
    for j in range(M-8+1):
        color=min(check_bw(j,i),check_wb(j,i))
        if 0==color: 
            print(0)
            exit()
        if min_color>color: min_color=color
print(min_color)
