N=int(input())
s=[-1]
for i in range(N):
   s.append(int(input()))
print(s)
c1=[-1 for _ in range(N+2)]
c2=[-1 for _ in range(N+2)]
c1[1]=s[1]

