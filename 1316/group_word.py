N=int(input())
count=N
for _ in range(N):
    s=input()
    visited=[False for _ in range(26)]
    for i,c in enumerate(s):
        index=ord(c)-ord('a')
        if True==visited[index]:
            if s[i-1]!=c:
                count-=1
                break;
        else:
            visited[index]=True
print(count)
