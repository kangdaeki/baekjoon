# to speed up the slow input()
import sys
input = sys.stdin.readline
nums=list(input())
nums.sort(reverse=True)
for n in nums:
    if n>="0" and n <="9": print(n,end="")
