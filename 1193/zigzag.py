import sys
input=sys.stdin.readline
X=int(input())
import math
total=math.ceil(-0.5+math.sqrt(2*X+0.25))
end=total*(total+1)//2
start=total*(total-1)//2+1
if 1==total%2: print("%d/%d"%(end+1-X,X-start+1))
else: print("%d/%d"%(X-start+1,end+1-X))
