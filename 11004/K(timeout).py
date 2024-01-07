# to speed up the slow input()
import sys
input = sys.stdin.readline

def partition(l:int,r:int,K:int)->int: # Hoare
    if l>=r: return l
    pivot=A[l]
    i=l+1
    j=r
    while i<=j:
        while i<=r and A[i]<=pivot: i+=1
        while j>=l+1 and A[j]>=pivot: j-=1
        if i<j: A[i],A[j]=A[j],A[i]
    if j<K<i: return K
    m=j+(i-j)//2
#    print(i,j,m)
    A[l],A[m]=A[m],A[l]
    return m

N,K=map(int,input().split())
K-=1 # list index starts from 0
A=list(map(int,input().split()))
#print(A.index(K))
l=0
r=len(A)-1
index=partition(l,r,K)
while index!=K:
    if index<K: l=index+1
    elif index>K: r=index-1
    else: break
    index=partition(l,r,K)
print(A[K])

