import sys
input=sys.stdin.readline
n=int(input())
stack=[]
for _ in range(n):
    s=list(input().split())
    if 'push'==s[0]:
        stack.append(int(s[1]))
    elif 'pop'==s[0]:
        if 0>=len(stack):
            print(-1)
        else:
            print(stack.pop())
    elif 'size'==s[0]:
        print(len(stack))
    elif 'empty'==s[0]:
        if 0>=len(stack): 
            print(1)
        else:
            print(0)
    elif 'top'==s[0]:
        if 0>=len(stack): 
            print(-1)
        else:
            print(stack[len(stack)-1])

