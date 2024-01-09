max_index=1
max_v=int(input())
for i in range(2,10):
    n=int(input())
    if max_v<n:
        max_v=n
        max_index=i
print(max_v)
print(max_index)

